# Analysis Qualifying Exam - January 2021

<a id="analysis-qualifying-exam---january-2021"></a>
## Problems

1. Let $(X\mathscr{,M,}\mu )$  be a measure space, and let $E_{n}\mathscr{\in M}$  be a measurable set for $n\geq 1$ . Let $f_{n}=\chi _{E_{n}}$ , the indicator function of the set $E_{n}$ . Prove that

1. $f_{n}\rightarrow 1$  uniformly, if and only if there exists $N\mathbb{\in N}$  such that $E_{n}=X$  for all $n\geq N$ .
2. $f_{n}(x)\rightarrow 1$  for almost every $x$ , if and only if

$$
\mu ​\left(\underset{n\geq 0}{\bigcap }\underset{k\geq n}{\bigcup }(X \textbackslash E_{k})\right)=0
$$

2. Calculate the limit:

$$
L:=\lim_{n\to \infty }\int_{0}^{n}\frac{cos(x/n)}{x^{2}+cos(x/n)} \, dx
$$

- Justify each step of your calculations!

3. Let $(X\mathscr{,M,}\mu )$  be a finite measure space. Let $\{f_{n}\}_{n=1}^{\infty }\subseteq L^{1}(X,\mu )$  and $f\in L^{1}(X,\mu )$  such that $f_{n}(x)\rightarrow f(x)$  as $n\rightarrow \infty$  for almost every $x\in X$ .

- Prove that for every $\varepsilon >0$  there exist $M>0$ , and a set $E\subseteq X$ , such that $\mu (E)\leq \varepsilon$  and $|f_{n}(x)|\leq M$  for all $x\in X \textbackslash E$  and all $n\mathbb{\in N}$ .

4. Let $f$  and $g$  be Lebesgue integrable on $\mathbb{R}$ . Let $g_{n}(x)=g(x-n)$ . Prove that

$$
\lim_{n\to \infty }\left\|f+g_{n}\right\|_{1}=\left\|f\right\|_{1}+\left\|g\right\|_{1}
$$

5. Let $f_{n}\in L^{2}[0,1]$  for $n\mathbb{\in N}$ . Assume that

1. $\left\|f_{n}\right\|_{2}\leq n^{-51/100}$ , for all $n\mathbb{\in N}$ , and
2. $\hat{f}_{n}$  is supported in the interval $[2^{n},2^{n+1}]$ , that is

$$
\hat{f}_{n}(k)=\int_{0}^{1}f_{n}(x)e^{-2\pi ikx} \, dx=0, for k\notin [2^{n},2^{n+1}].
$$

- Prove that $\sum_{n=1}^{\infty }f_{n}$  converges in the Hilbert space $L^{2}([0,1])$ .
- (Hint: Plancherel's identity may be helpful.)

6. Let $f\mathbb{:R\times R\rightarrow R}$  be a measurable function, and for $x\mathbb{\in R}$  define the set

$$
E_{x}:=\{ \, y\mathbb{\in R:}m(\{z\mathbb{\in R:}f(x,z)=f(x,y)\})>0 \, \}.
$$

- Show that

$$
E:=\underset{x}{\bigcup }\{x\}\times E_{x}
$$

- is a measurable subset of $\mathbb{R\times R}$ .
- (Hint: consider the measurable function $h(x,y,z):=f(x,y)-f(x,z)$ .)