# Real Analysis Qualifying Examination, January 2008

<a id="main-content"></a>
## Instructions

There are five problems, each worth 20 points. Give complete justification for all assertions by either citing known theorems or giving arguments from first principles.

<a id="problems-heading"></a>
## Problems

1. For $n\mathbb{\in N}$ , let $u_{n}(x)=\frac{ln(1+x^{n})}{n}$ . For which $x\mathbb{\in R}$  does $f(x)=\sum_{n=1}^{\infty }u_{n}(x)$  converge? For which $x\mathbb{\in R}$  is $f$  differentiable?

1. Provide an example of a function $f:\mathbb{R}^{2}\mathbb{\rightarrow R}$  which is continuous when restricted to any line through the origin, but is not continuous at the origin. (Give complete explanations of why your example has the desired property.)
2. Provide an example of a function $f:\mathbb{R}^{2}\mathbb{\rightarrow R}$  which is everywhere differentiable when restricted to any line through the origin but is not differentiable at the origin. (Again, be sure to give complete justification that your example works.)

1. Let $E\subseteq [0,1)$  be a Lebesgue measurable set. Prove that

$$
\int_{E}^{​}sin(2\pi nx) \, dx\rightarrow 0 \quad as \quad n\rightarrow \infty
$$

- by exploiting the fact that $\{e^{2\pi inx}\}_{n\mathbb{\in Z}}$  is an orthonormal set in $L^{2}[0,1)$ .

2. Show that the above also holds for any measurable set $E\mathbb{\subseteq R}$  of finite measure.

2. Let $A,B\mathbb{\subset R}$  be two Lebesgue measurable sets of finite measure. For $x\mathbb{\in R}$  define the function:

$$
f(x)=m(A\cap (B+x))
$$

- where $B+x=\{b+x \, ; \, b\in B\}$  is the translate of the set $B$  by $x$ .
- Prove that $f$  is measurable, and

$$
\int_{\mathbb{R}}^{​}f(x) \, dx=m(A)m(B).
$$

3. Let $\{f_{k}\}$  be a sequence of functions in $L^{1}\mathbb{(R)}$  which converges, in the $L^{1}$  sense, to some function $f\in L^{1}\mathbb{(R)}$ . Prove that there is a subsequence of $\{f_{k}\}$  which converges pointwise almost everywhere to $f$ .