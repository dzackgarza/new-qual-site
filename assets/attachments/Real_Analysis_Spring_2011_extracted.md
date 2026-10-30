# Real Analysis Qualifying Examination — January 2011

There are five problems, each worth 20 points. Give complete justification for all assertions by either citing known theorems or giving arguments from first principles.

Notation: In Questions 3 and 4 below $m$  stands for Lebesgue measure on $\mathbb{R}$ .

<a id="problems"></a>
## Problems

1. Let $A\subseteq \mathbb{R}^{n}$ . Give a precise definition of what it means for a function $f:A\mathbb{\rightarrow R}$  to be uniformly continuous on $A$ .
2. Let $K$  be a compact subset of $\mathbb{R}^{n}$ . Prove that if $f:K\mathbb{\rightarrow R}$  is continuous on $K$ , then $f$  is uniformly continuous on $K$ .

1. Let $0<p<\infty$  and $\{x_{n}\}_{n=1}^{\infty }$  be a bounded sequence of complex numbers. Prove the equivalence of the following two statements:

1. $lim_{N\rightarrow \infty }\frac{1}{N}\sum_{n=1}^{N}|x_{n}|^{p}=0$
2. For every $\varepsilon >0$ , $lim_{N\rightarrow \infty }\frac{1}{N}\left|\left\{1\leq n\leq N:|x_{n}|\geq \varepsilon \right\}\right|=0$

2. Let $f$  be a Lebesgue integrable function on $\mathbb{R}$ . Prove that for every $\varepsilon >0$  there exists $\delta >0$  such that

$$
\int_{E}^{​}|f(x)| \, dx<\varepsilon
$$

- whenever $m(E)<\delta$ .

3. Let $A,B\mathbb{\subseteq R}$  be bounded measurable sets with positive Lebesgue measure. For each $t\mathbb{\in R}$  define the function

$$
g(t)=m\left(A\cap (t-B)\right)
$$

- where $t-B=\{t-b:b\in B\}$ .

1. Prove that $g$  is a continuous function and

$$
\int_{\mathbb{R}}^{​}g(t) \, dt=m(A)m(B).
$$

2. Conclude that the sumset

$$
A+B=\{a+b:a\in A and b\in B\}
$$

- contains a non-empty open subset of $\mathbb{R}$ .

4. Let $1\leq p<q<\infty$ .

1. Which of the following statements (i)-(iv) are true, and which are false? Justify all the negative answers by a counterexample and all positive answers with a proof.

1. $L^{p}\mathbb{(R)\subseteq}L^{q}\mathbb{(R)}$
2. $L^{q}\mathbb{(R)\subseteq}L^{p}\mathbb{(R)}$
3. $L^{p}([0,1])\subseteq L^{q}([0,1])$
4. $L^{q}([0,1])\subseteq L^{p}([0,1])$

2. Justify your answer to the following question:

- For which values of $r\geq 1$  is it true that $L^{p}\mathbb{(R)\cap}L^{q}\mathbb{(R)\subseteq}L^{r}\mathbb{(R)}$ ?