# Real Analysis Qualifying Exam, January 2012

PRINT NAME:

<a id="real-analysis-qualifying-exam"></a>
## Instructions

Give clear reasoning. State clearly which theorem(s) you are using. Cross out the parts you do not want to be graded. Read through all the problems, do them in any order - the ones you feel most confident first. You should not cite anything else: examples, exercises, or problems.

<a id="graders-comments"></a>
## Grader's Comments

<a id="notation"></a>
## Notation

$\mathbb{R}$  is the set of real numbers; $m$  is the Lebesgue measure.

<a id="problems"></a>
## Problems

1. Let $f_{n}(x)=\frac{x}{1+nx^{2}}$ , $x\mathbb{\in R}$ . Show that

1. $f_{n}$  converges uniformly to a function $f$ , and
2. $f^{'}(x)=lim_{n\rightarrow \infty }f_{n}^{'}(x)$  is true for $x\ne 0$ , and false for $x=0$ .

2. Show that there is $\varepsilon >0$  such that if $|x|<\varepsilon$  then

$$
\int_{0}^{x}e^{t^{2}} \, dt>\frac{x^{2}}{2}+ln(1+x)
$$

3. Let $E\subset [0,\infty )$  be a measurable set with $p:=m(E)>0$ . Show that for any number $c\in [0,p)$ , there is a number $x\in [0,\infty )$  such that $m([0,x]\cap E)=c$ .
4. Let $f\mathbb{:R\rightarrow R}$  be a nonnegative integrable function.

1. Show that $sin\circ f$  is integrable.
2. Use Fubini's theorem to show that

$$
\int_{[0,\infty )}^{​}m(\{x:f(x)\geq y\})cosy \, dy=\int_{\mathbb{R}}^{​}sin(f(x)) \, dx.
$$

5. Let $p\in [1,\infty )$ , and suppose that $f\mathbb{:R\rightarrow R}$  is an absolutely continuous function such that $\parallel f^{'}\parallel _{p}<\infty$ .

1. Prove that $f$  is Hölder continuous with exponent $\frac{p-1}{p}$ , i.e. there is a constant $C$  such that

$$
|f(x)-f(y)|\leq C|x-y|^{\frac{p-1}{p}}.
$$

2. Write down the corresponding statement when $p=\infty$  and prove your assertion.

6. Let $V$  be the vector space of absolutely continuous functions on $[0,1]$  endowed with the following norm

$$
\parallel f\parallel :=\int_{0}^{1}|f(t)| \, dt+\int_{0}^{1}|f^{'}(t)| \, dt, \quad \quad f\in V.
$$

- Show that $(V,\parallel \cdot \parallel )$  is a Banach space. You do not need to prove that $\parallel \cdot \parallel$  is a norm.