# Real Analysis Qualifying Examination, Fall 2020

The five problems on this exam have equal weighting. To receive full credit give complete justification for all assertions by either citing known theorems or giving arguments from first principles.

<a id="problems"></a>
## Problems

1. Show that if $x_{n}$  is a decreasing sequence of positive real numbers such that $\sum_{n=1}^{\infty }x_{n}$  converges, then

$$
\lim_{n\to \infty }nx_{n}=0.
$$

1. Let $f\mathbb{:R\rightarrow R}$ . Prove that

$$
f(x)\leq \underset{y\to x}{liminf}f(y) for each x\mathbb{\in R} \quad \Leftrightarrow \quad \{x\mathbb{\in R:}f(x)>a\} is open for all a\mathbb{\in R.}
$$

2. Recall that a function $f\mathbb{:R\rightarrow R}$  is called lower semi-continuous if it satisfies either condition in part (a) above. Prove that if $\mathscr{F}$  is any family of lower semi-continuous functions, then

$$
g(x)=sup\{f(x):f\mathscr{\in F\}}
$$

- is Borel measurable. Note that $\mathscr{F}$  need not be a countable family.

2. Let $f$  be a non-negative Lebesgue measurable function on $[1,\infty )$ .

1. Prove that

$$
1\leq \left(\frac{1}{b-a}\int_{a}^{b}f(x) \, dx\right)\left(\frac{1}{b-a}\int_{a}^{b}\frac{1}{f(x)} \, dx\right)
$$

- for any $1\leq a<b<\infty$ .

2. Prove that if $f$  satisfies

$$
\int_{1}^{t}f(x) \, dx\leq t^{2}logt
$$

- for all $t\in [1,\infty )$ , then

$$
\int_{1}^{\infty }\frac{1}{f(x)} \, dx=\infty .
$$

- Hint: Write $\int_{1}^{\infty }\frac{1}{f(x)} \, dx=\sum_{k=0}^{\infty }\int_{2^{k}}^{2^{k+1}}\frac{1}{f(x)} \, dx.$

3. Prove that if $xf\in L^{1}\mathbb{(R)}$ , then

$$
F(y):=\int_{\mathbb{R}}^{​}f(x)cos(yx) \, dx
$$

- defines a $C^{1}$  function.

4. Suppose $\varphi \in L^{1}\mathbb{(R)}$  with $\int_{\mathbb{R}}^{​}\varphi (x) \, dx=a$ . For each $\delta >0$  and $f\in L^{1}\mathbb{(R)}$  define

$$
\mathscr{A}_{\delta }f(x):=\int_{\mathbb{R}}^{​}f(x-y) \, \delta ^{-1}\varphi ​\left(\delta ^{-1}y\right) \, dy.
$$

1. Prove that $\left\|\mathscr{A}_{\delta }f\right\|_{1}\leq \parallel \varphi \parallel _{1}\parallel f\parallel _{1}$  for all $\delta >0$ .
2. Prove that $\mathscr{A}_{\delta }f\rightarrow af$  in $L^{1}\mathbb{(R)}$  as $\delta \rightarrow 0^{+}$ .

- Hint: You may use, without proof, the fact that $lim_{y\rightarrow 0}\int_{\mathbb{R}}^{​}|f(x-y)-f(x)| \, dx=0$  for all $f\in L^{1}\mathbb{(R)}$ .