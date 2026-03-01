Farida Noori
Lab4: Part A: Questions about the video

1.	What sorting algorithm was the speaker trying to improve? 
The speaker was trying to improve introsort (introspective sort), the hybrid algorithm used in most C++ standard library implementations of std::sort (combining quicksort with heapsort fallback for worst-case guarantee).

2.	At what partition size does VS perform a simpler sort algorithm instead of continuing to partition?
Visual Studio's implementation (Microsoft STL) switches to a simpler sort (insertion sort) at a partition size of 32.

3.	At what partition size does GNU perform a simpler sort algorithm instead of continuing to partition? 
GNU's libstdc++ (GCC) switches to insertion sort at a partition size of 16.

4.	Regular insertion sort does a linear search backwards from end of array for correct spot to insert. According to the speaker, why does switching to a binary search not improve performance? 
Switching to binary search for the insertion point does not improve performance because the bottleneck in small-array insertion sort is not finding the position (comparisons), but moving elements to make space for the insertion. Binary search reduces comparisons slightly but increases overall moves or complexity without enough gain, and branch mispredictions or cache effects can even hurt it.

5.	Describe what is meant by branch prediction. 
Branch prediction is a CPU technique to guess the outcome of conditional branches (if/else, loops) ahead of time so the pipeline can keep fetching instructions without stalling. Modern CPUs use hardware predictors (based on history patterns) to speculate. If the prediction is wrong (misprediction), the CPU flushes the pipeline and fetches the correct path, costing many cycles (often 10–20+). In sorting, unpredictable branches (e.g., random comparison outcomes) cause frequent mispredictions, slowing execution significantly.

6.	What is meant by the term informational entropy? 
Informational entropy (from information theory) measures the uncertainty or randomness in a dataset. For a sequence to be sorted, entropy is high when elements are in random order (maximum uncertainty about positions) and low (zero) when fully sorted. In sorting contexts, algorithms that exploit low-entropy patterns (nearly sorted data) can perform better, but random data has high entropy, forcing more work. The speaker relates it to how predictable branches are—high entropy leads to poor branch prediction.

7.	Speaker suggests the following algorithm:
make_heap() then unguarded_insertion_sort(). He suggests that by doing make_heap() first, you can do something called unguarded_insertion_sort(). Please explain what unguarded_insertion_sort() is and why it is faster than regular insertion sort. How does performing make_heap() allow you to do this? 
unguarded_insertion_sort() is a variant of insertion sort that omits the bounds check on the left side of the array when searching for the insertion point. Regular insertion sort must check if the search has gone past the beginning to avoid reading invalid memory. By first calling make_heap() on the entire range (turning it into a max-heap), the largest element is guaranteed to be at the front (position 0). When inserting later elements via insertion sort, the search loop can assume it will always find a spot before reaching the beginning (because any element is ≤ the heap root, which is largest). This removes the need for a guard/conditional check in the inner loop, reducing branches and improving predictability/speed. It trades heap construction cost for cheaper insertions.

8.	The speaker talks about incorporating your conditionals into your arithmetic. What does this mean? Provide an example from the video and explain how the conditional is avoided. 
This means replacing branchy code (if/else conditionals) with branchless arithmetic operations (e.g., using min/max, bitwise ops, or conditional moves) that the CPU can execute without branching. Branches risk mispredictions; arithmetic is predictable and pipelinable. An example from the talk is in the partition scheme (likely Lomuto or similar): instead of if (a < pivot) ... else ..., use arithmetic like bool less = a < pivot; left += less; *left = less ? a : *right; or similar tricks (e.g., with masks or cmov). This folds the conditional decision into index calculations or selections, avoiding unpredictable branches and improving throughput.

9.	The speaker talks about a bug in gnu's implementation. Describe the circumstances of this bug. 
The bug in GNU's (libstdc++) introsort implementation occurs when the array has exactly 2 elements that are out of order. In certain partition or small-sort paths, it fails to swap them correctly or enters an inconsistent state, leading to incorrect sorting or infinite loops in edge cases. (The speaker highlights this as an example of overlooked small cases in production code.)

10.	The speaker shows several graphs about what happens as the threshold increases using his new algorithm. The metric of comparison is increased, and the metric of moves is increased, but time drops... What metric does the author think is missing? Describe the missing metric he speaks about in the video. What is the metric measuring? 
The missing metric is branch mispredictions (or mispredicted branches per element). Even though comparisons and element moves increase slightly with higher thresholds (larger insertion sort ranges), the time decreases because the code has fewer unpredictable branches and better branch prediction accuracy. The speaker argues that modern performance analysis must include branch misprediction costs (alongside instructions, cache misses, etc.), as they dominate in tight loops like sorting.

11.	What does the speaker mean by fast code is left-leaning? 
"Fast code is left-leaning" refers to structuring conditionals so the common/fast path is the "then" branch (left side in code), and the rare/slow path is the "else". CPUs often predict forward branches (then) as not-taken or taken depending on static hints, but more importantly, it aligns with how predictors learn patterns—keeping hot paths predictable and minimizing mispredictions on frequent cases.

12.	What does the speaker mean by not mixing hot and cold code? 
"Not mixing hot and cold code" means separating frequently executed ("hot") code paths from rarely executed ("cold") code (e.g., error handling, unlikely conditions). Mixing them in the same function or cache line causes cache pollution: cold code evicts hot instructions from L1 cache, or branches to cold paths cause mispredictions and bring in unused code. The speaker advocates hoisting cold code out (e.g., via __builtin_expect, separate functions, or attributes) to keep instruction cache focused on hot paths for better performance.


Part B: Reflection

1.	What did you/your team find most challenging to understand in the video? 
The most challenging part was grasping why doing more work (like building a full heap upfront and accepting slightly higher comparison/move counts) could actually make the overall sorting faster, especially on already-sorted or nearly-sorted data. In theory, insertion sort shines on sorted input with almost zero work, so seeing a 9% speedup after extra heap construction felt deeply counterintuitive. The connection between branch prediction, predictability of linear vs. binary search, and how modern CPUs punish unpredictable branches more than extra instructions was also hard to fully internalize at first—it requires thinking about hardware behavior rather than just algorithmic big-O complexity.

2.	What is the most surprising thing you learned that you did not know before? 
The biggest surprise was how dominant branch mispredictions can be in performance, even more than raw comparison or move counts. I had no idea that a "worse" algorithm in terms of operations (e.g., linear search in insertion sort) could outperform a "smarter" one (binary search for insertion point) purely because the branches are far more predictable (often 90%+ hit rate vs. ~50% for binary). Another mind-blowing point was the heap + unguarded insertion trick: by paying the cost to make_heap() first, you eliminate bounds checks in the insertion loop forever after, turning a potentially branchy guard condition into pure arithmetic. The fact that this wins even on sorted arrays—where you'd expect zero benefit—was completely unexpected.

3.	Has the video given you ideas on how you can write better/faster code? If yes, explain what you plan to change when writing code in the future. If not, explain why not. 
Yes, absolutely—this talk has changed how I approach performance-critical code. In the future, I plan to:
o	Profile branch mispredictions (using tools like perf or VTune) instead of only looking at instruction counts or cache misses.
o	Favor predictable, "boring" code over clever but unpredictable branches (e.g., prefer linear patterns that the branch predictor can learn easily).
o	Consider branchless alternatives or arithmetic tricks (like using min/max or conditional moves) to reduce unpredictable control flow.
o	Avoid mixing hot and cold code paths in the same function, and use attributes like __builtin_expect to hint the likely path.
o	Think more about micro-optimizations for small inputs since they dominate in recursive algorithms like sorting or tree traversals. Overall, the talk reinforced that real speed often comes from understanding the machine's "mind" (predictors, caches, pipelines) rather than just elegant algorithms. I'll be more willing to try "silly" ideas and measure obsessively instead of assuming theory alone will guide me.

References
•	Video: https://www.youtube.com/watch?v=FJJTYQYB1JQ
•	Algorithmica HPC branch/cache articles (as provided): https://en.algorithmica.org/hpc/
•	CppCon slides: https://github.com/CppCon/CppCon2019 (search for Andrei's talk)

