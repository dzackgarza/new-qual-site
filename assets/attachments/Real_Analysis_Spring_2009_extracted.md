# Real Analysis Qualifying Examination — January 2009

<a id="real-analysis-qualifying-examination"></a>
## Instructions

There are five problems, each worth 20 points. Give complete justification for all assertions by either citing known theorems or giving arguments from first principles.

<a id="problems"></a>
## Problems

1. Let $f:[0,1\mathbb{]\rightarrow R}$  be continuous. Evaluate

$$
\lim_{k\to \infty }\int_{0}^{1}kx^{k-1}f(x) \, dx
$$

2. Let $\mathscr{B}$  denote the set of all Borel subsets of $\mathbb{R}$ . Let $\mu \mathscr{:B\rightarrow [}0,\infty )$  be a set function with the property that if $\{E_{k}\}$  is a countable collection of disjoint sets in $\mathscr{B}$ , then

$$
\mu ​\left(\underset{k=1}{\overset{\infty }{\bigcup }}E_{k}\right)=\sum_{k=1}^{\infty }\mu (E_{k}).
$$

1. Prove that if $\{F_{k}\}$  is a sequence of Borel sets for which $F_{k}\supset F_{k+1}$  for all $k$ , then

$$
\lim_{k\to \infty }\mu (F_{k})=\mu ​\left(\underset{k=1}{\overset{\infty }{\bigcap }}F_{k}\right).
$$

2. Suppose that for every $E\mathscr{\in B}$  with Lebesgue measure $m(E)=0$ , it follows that $\mu (E)=0$ .

- Prove that for every $\varepsilon >0$  there exists $\delta >0$  so that if $E\mathscr{\in B}$  with $m(E)<\delta$ , then $\mu (E)<\varepsilon$ .

3. Let $\{f_{k}\}$  be any sequence of functions in $L^{2}([0,1])$  satisfying $\parallel f_{k}\parallel _{2}\leq M$  for all $k\mathbb{\in N}$ . Prove that if $f_{k}\rightarrow f$  almost everywhere, then

$$
\lim_{k\to \infty }\int_{0}^{1}f_{k}(x) \, dx=\int_{0}^{1}f(x) \, dx
$$

1. Show that if $f\in L^{4}([0,1])$ , then $f\in L^{2}([0,1])$  and $\parallel f\parallel _{2}\leq \parallel f\parallel _{4}$ .
2. Does there exist a constant $C$  so that for all $f\in L^{4}([0,1])$ , $\parallel f\parallel _{4}\leq C\parallel f\parallel _{2}$ ? Justify your answer.
3. For a fixed function $g\in L^{4}([0,1])$ , let $A$  denote the ratio $\parallel g\parallel _{4}/\parallel g\parallel _{2}$ . Find a constant $B$ , depending only on $A$ , such that $\parallel g\parallel _{2}\leq B\parallel g\parallel _{1}$ .

4. Let $\mathscr{H}$  be a Hilbert space and $\{\varphi _{k}\}_{k=1}^{\infty }$  be a subset of $\mathscr{H}$  with the property that for every $f\mathscr{\in H}$

$$
\sum_{k=1}^{\infty }\left|\left⟨f,\varphi _{k}\right⟩\right|^{2}=\parallel f\parallel ^{2}
$$

- where $\left⟨f,\varphi _{k}\right⟩$  denotes the inner product of $f$  and $\varphi _{k}$  in $\mathscr{H}$  and $\parallel f\parallel$  denotes the norm of $f$  on $\mathscr{H}$ .

1. Show that for all $f,g$  in $\mathscr{H}$ ,

$$
\langle f,g\rangle =\sum_{k=1}^{\infty }\left⟨f,\varphi _{k}\right⟩\overline{\left⟨g,\varphi _{k}\right⟩}
$$

- [Hint: Consider $\parallel f+g\parallel ^{2}$  and $\parallel f+ig\parallel ^{2}$ ]

2. Show that for all $f$  in $\mathscr{H}$ ,

$$
\lim_{N\to \infty }\left\|f-\sum_{k=1}^{N}\left⟨f,\varphi _{k}\right⟩\varphi _{k}\right\|=0
$$

- [Hint: Use the fact that $\parallel h\parallel =sup_{\parallel g\parallel \leq 1}|\langle h,g\rangle |$  for all $h$  in $\mathscr{H}$ ]