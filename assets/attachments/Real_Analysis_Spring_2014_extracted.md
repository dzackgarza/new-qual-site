# Real Analysis Qualifying Examination, Spring 2014

<a id="real-analysis-qualifying-examination"></a>
## Instructions

There are five problems, each worth 20 points. Give complete justification for all assertions by either citing known theorems or giving arguments from first principles.

<a id="problems"></a>
## Problems

1. Give an example of a continuous function $f$  in $L^{1}\mathbb{(R)}$  for which $f(x)\nrightarrow 0$  as $|x|\rightarrow \infty$ .
2. Prove that if $f\in L^{1}\mathbb{(R)}$  and uniformly continuous, then $lim_{|x|\rightarrow \infty }f(x)=0$ .

1. Let $\{a_{n}\}$  be a sequence of non-negative real numbers such that $\sum_{n=1}^{\infty }a_{n}b_{n}<\infty$  for any given sequence $\{b_{n}\}$  of non-negative real numbers for which $\sum_{n=1}^{\infty }b_{n}^{2}<\infty$ . Prove that $\sum_{n=1}^{\infty }a_{n}^{2}<\infty$ .
2. Suppose $f\mathbb{:R\rightarrow R}$  satisfies

$$
f(x)\geq \underset{y\to x}{limsup}f(y)
$$

- for all $x\mathbb{\in R}$ . Prove that $f$  is Borel measurable.

3. Let $(X,\mu )$  be a finite measure space and $f$  be a non-negative measurable function on $X$ .

- Prove that $lim_{n\rightarrow \infty }\int_{X}^{​}f^{n} \, d\mu$  is either $\infty$  or $\mu ​\left(f^{-1}(1)\right)$ , and characterize the collection of functions $f$  of each type.

4. Let $f,g\in L^{1}([0,1])$  and for each $0\leq x\leq 1$  define

$$
F(x):=\int_{0}^{x}f(y) \, dy \quad and \quad G(x):=\int_{0}^{x}g(y) \, dy.
$$

- Prove that

$$
\int_{0}^{1}F(x)g(x) \, dx=F(1)G(1)-\int_{0}^{1}f(x)G(x) \, dx.
$$