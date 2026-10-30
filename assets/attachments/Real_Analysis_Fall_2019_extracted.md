# Real Analysis Qualifying Examination — August 2019

<a id="real-analysis-qualifying-examination"></a>
## Instructions

The five problems on this exam have equal weighting.

To receive full credit give complete justification for all assertions by either citing known theorems or giving arguments from first principles.

<a id="problems"></a>
## Problems

1. Let $\left\{a_{n}\right\}_{n=1}^{\infty }$  be a sequence of real numbers.

1. Prove that if $lim_{n\rightarrow \infty }a_{n}=0$ , then $lim_{n\rightarrow \infty }\frac{a_{1}+\cdots +a_{n}}{n}=0$ .
2. Prove that if $\sum_{n=1}^{\infty }\frac{a_{n}}{n}$  converges, then $lim_{n\rightarrow \infty }\frac{a_{1}+\cdots +a_{n}}{n}=0$ .

2. Prove that

$$
\left|\frac{d^{n}}{dx^{n}}\frac{sinx}{x}\right|\leq \frac{1}{n}
$$

- for all $x\ne 0$  and positive integers $n$ .
- Hint: Consider $\int_{0}^{1}cos(tx) \, dt$ .

3. Let $(X\mathscr{,B,}\mu )$  be a measure space with $\mu (X)=1$ , $\left\{B_{n}\right\}_{n=1}^{\infty }$  be a sequence of $\mathscr{B}$ -measurable subsets of $X$ , and $B:=\{x\in X:x\in B_{n} for infinitely many n\}$ .

1. Argue that $B$  is also a $\mathscr{B}$ -measurable subset of $X$ .
2. Prove that if $\sum_{n=1}^{\infty }\mu (B_{n})<\infty$ , then $\mu (B)=0$ .
3. Prove that if $\sum_{n=1}^{\infty }\mu (B_{n})=\infty$  and the sequence of set complements $\left\{B_{n}^{c}\right\}_{n=1}^{\infty }$  satisfies

$$
\mu ​\left(\underset{n=k}{\overset{K}{\bigcap }}B_{n}^{c}\right)=\prod_{n=k}^{K}\left(1-\mu (B_{n})\right)
$$

- for all positive integers $k$  and $K$  with \(k

- Hint: Use the fact that $1-x\leq e^{-x}$  for all $x$ .

4. Let $\left\{u_{n}\right\}_{n=1}^{\infty }$  be an orthonormal sequence in a Hilbert space $\mathscr{H}$ .

1. Prove that for every $x\mathscr{\in H}$  one has $\sum_{n=1}^{\infty }\left|\left⟨x,u_{n}\right⟩\right|^{2}\leq \parallel x\parallel ^{2}$ .
2. Prove that for any sequence $\left\{a_{n}\right\}_{n=1}^{\infty }$  in $\mathscr{l}^{2}\mathbb{(N)}$  there exists an element $x$  in $\mathscr{H}$  such that $a_{n}=\left⟨x,u_{n}\right⟩$  for all $n\mathbb{\in N}$  and $\parallel x\parallel ^{2}=\sum_{n=1}^{\infty }\left|\left⟨x,u_{n}\right⟩\right|^{2}$ .

1. Show that if $f$  is continuous with compact support on $\mathbb{R}$ , then

$$
\lim_{y\to 0}\int_{\mathbb{R}}^{​}|f(x-y)-f(x)| \, dx=0
$$

2. Let $f\in L^{1}\mathbb{(R)}$  and for each $h>0$  let $\mathscr{A}_{h}f(x):=\frac{1}{2h}\int_{|y|\leq h}^{​}f(x-y) \, dy$ .

1. Prove that $\parallel \mathscr{A}_{h}f\parallel _{1}\leq \parallel f\parallel _{1}$  for all $h>0$ .
2. Prove that $\mathscr{A}_{h}f\rightarrow f$  in $L^{1}\mathbb{(R)}$  as $h\rightarrow 0^{+}$ .