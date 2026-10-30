# Real Analysis Qualifying Exam, January 2007

<a id="Xc2b9ab771038c6d939aedb898d8e6a16aaee807"></a>
## Instructions

This is a two-hour exam. The problems are weighted equally. Throughout the exam, $(\Omega ,\mathscr{M,}\mu )$  denotes a measure space.

<a id="problems"></a>
## Problems

1. Let $f\mathbb{:R\rightarrow R}$  be a continuously differentiable function. Let $g:\mathbb{R}^{2}\mathbb{\rightarrow R}$  be defined by

$$
g(x,y)=\left\{\begin{matrix}\frac{f(x)-f(y)}{x-y}&x\ne y,\\f^{'}(x)&x=y.\end{matrix}\right.
$$

- Prove that $g$  is continuous.

2. Let $\{E_{i}\}$  be a sequence of measurable subsets of $\Omega$  such that $\sum_{i}^{​}\mu (E_{i})<\infty$ . Set

$$
S=\{\omega \in \Omega \mid \omega \in E_{i} for infinitely many i\}.
$$

- Show that $\mu (S)=0$ .

3. A set $\Phi \subset L^{1}(\Omega )$  is said to be uniformly integrable if, for each $\epsilon >0$  there exists $\delta >0$  such that whenever $f\in \Phi$  and $E\subset \Omega$  is measurable with $\mu (E)<\delta$ , we have $\int_{E}^{​}|f| \, d\mu <\epsilon$ .

- Assume $\mu (\Omega )=1$  and suppose $\{f_{n}\}_{n\mathbb{\in N}}$  is a uniformly integrable sequence of functions, such that $f_{n}\rightarrow 0$  almost everywhere. Prove that

$$
\lim_{n\to \infty }\int_{\Omega }^{​}|f_{n}| \, d\mu =0.
$$

4. Let $f\in L^{\infty }(\Omega )\cap L^{1}(\Omega )$ . Show that $lim_{p\rightarrow \infty }\parallel f\parallel _{p}=\parallel f\parallel _{\infty }$ . (Hint: $|f|^{p}=|f| \, |f|^{p-1}$ .)
5. Let $I$  denote the unit interval, equipped with Lebesgue measure. Suppose $f\in L^{2}(I)$  and $F\in L^{2}(I\times I)$ . For each $x\in I$  at which the integral exists, set

$$
g(x)=\int_{I}^{​}f(y)F(x,y) \, dy.
$$

- Show that $g(x)$  exists almost everywhere, and that $\parallel g\parallel _{2}\leq \parallel f\parallel _{2}\parallel F\parallel _{2}$ .

6. Let $X$  be a Banach space. State the definition of the dual Banach space, $X^{*}$ , and prove that $X^{*}$  is complete.