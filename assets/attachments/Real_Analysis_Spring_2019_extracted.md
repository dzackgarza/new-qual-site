# Real Analysis Qualifying Examination, Spring 2019

<a id="real-analysis-qualifying-examination"></a>
## Instructions

The five problems on this exam have equal weighting. To receive full credit give complete justification for all assertions by either citing known theorems or giving arguments from first principles.

<a id="problems"></a>
## Problems

1. Let $C([0,1])$  denote the space of all continuous real-valued functions on $[0,1]$ .

1. Prove that $C([0,1])$  is complete under the uniform norm $\parallel f\parallel _{u}:=sup_{x\in [0,1]}|f(x)|$ .
2. Prove that $C([0,1])$  is not complete under the $L^{1}$ -norm $\parallel f\parallel _{1}=\int_{0}^{1}|f(x)| \, dx$ .

2. Let $\mathscr{B}$  denote the set of all Borel subsets of $\mathbb{R}$  and $\mu \mathscr{:B\rightarrow [}0,\infty )$  denote a finite Borel measure on $\mathbb{R}$ .

1. Prove that if $\{F_{k}\}$  is a sequence of Borel sets for which $F_{k}\supseteq F_{k+1}$  for all $k$ , then

$$
\lim_{k\to \infty }\mu (F_{k})=\mu ​\left(\underset{k=1}{\overset{\infty }{\bigcap }}F_{k}\right).
$$

2. Suppose $\mu$  has the property that $\mu (E)=0$  for every $E\mathscr{\in B}$  with Lebesgue measure $m(E)=0$ . Prove that for every $\varepsilon >0$  there exists $\delta >0$  so that if $E\mathscr{\in B}$  with $m(E)<\delta$ , then $\mu (E)<\varepsilon$ .

3. Let $\{f_{k}\}$  be any sequence of functions in $L^{2}([0,1])$  satisfying $\parallel f_{k}\parallel _{2}\leq M$  for all $k\mathbb{\in N}$ .

- Prove that if $f_{k}\rightarrow f$  almost everywhere, then $f\in L^{2}([0,1])$  with $\parallel f\parallel _{2}\leq M$  and

$$
\lim_{k\to \infty }\int_{0}^{1}f_{k}(x) \, dx=\int_{0}^{1}f(x) \, dx
$$

- Hint: Try using Fatou's Lemma to show that $\parallel f\parallel _{2}\leq M$  and then try applying Egorov's Theorem.

4. Let $f$  be a non-negative function on $\mathbb{R}^{n}$  and $\mathscr{A=}\left\{(x,t)\in \mathbb{R}^{n}\mathbb{\times R:}0\leq t\leq f(x)\right\}$ .

- Prove the validity of the following two statements:

1. $f$  is a Lebesgue measurable function on $\mathbb{R}^{n}\mathscr{\Leftrightarrow A}$  is a Lebesgue measurable subset of $\mathbb{R}^{n+1}$
2. If $f$  is a Lebesgue measurable function on $\mathbb{R}^{n}$ , then

$$
m\mathscr{(A)=}\int_{\mathbb{R}^{n}}^{​}f(x) \, dx=\int_{0}^{\infty }m​\left(\left\{x\in \mathbb{R}^{n}:f(x)\geq t\right\}\right) \, dt
$$

5. (a) Show that $L^{2}([0,1])\subseteq L^{1}([0,1])$  and argue that $L^{2}([0,1])$  in fact forms a dense subset of $L^{1}([0,1])$ .

- (b) Let $\Lambda$  be a continuous linear functional on $L^{1}([0,1])$ .
- Prove the Riesz Representation Theorem for $L^{1}([0,1])$  by following the steps below:

1. Establish the existence of a function $g\in L^{2}([0,1])$  which represents $\Lambda$  in the sense that

$$
\Lambda (f)=\int_{0}^{1}f(x) \, \overline{g(x)} \, dx \quad for all f\in L^{2}([0,1]).
$$

- Hint: You may use, without proof, the Riesz Representation Theorem for $L^{2}([0,1])$ .

2. Argue that the $g$  obtained above must in fact belong to $L^{\infty }([0,1])$  and represent $\Lambda$  in the sense that

$$
\Lambda (f)=\int_{0}^{1}f(x) \, \overline{g(x)} \, dx \quad for all f\in L^{1}([0,1])
$$

- with

$$
\parallel g\parallel _{L^{\infty }([0,1])}=\parallel \Lambda \parallel _{L^{1}([0,1])^{*}}.
$$