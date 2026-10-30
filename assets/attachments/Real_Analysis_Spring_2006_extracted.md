# Analysis Qualifying Exam: Real Analysis (January 6, 2006)

PRINT NAME:   
SIGNATURE:

<a id="analysis-qualifying-exam-real-analysis"></a>
# Analysis Qualifying Exam: Real Analysis

January 6, 2006

<a id="instructions"></a>
## Instructions

Give clear reasoning. State clearly which theorem you are using. Cross out the parts you do not want to be graded. Read through all the problems, do them in any order, the one you feel most confident about first. They are not in the order of difficulty. You should not cite anything else: examples, exercises, or problems.

<table><thead><tr><th><p>Problem #</p></th><th><p>Points</p></th><th><p>Score</p></th></tr></thead><tbody><tr><td><p>1</p></td><td><p>10</p></td><td></td></tr><tr><td><p>2</p></td><td><p>15</p></td><td></td></tr><tr><td><p>3</p></td><td><p>15</p></td><td></td></tr><tr><td><p>4</p></td><td><p>20</p></td><td></td></tr><tr><td><p>5</p></td><td><p>20</p></td><td></td></tr><tr><td><p>6</p></td><td><p>20</p></td><td></td></tr><tr><td><p>Total</p></td><td><p>100</p></td><td></td></tr></tbody></table>

Committee Recommendation

Grader's Remark

<a id="problems"></a>
## Problems

1. Define a sequence recursively by $a_{n+1}=\sqrt{2a_{n}}$ , $a_{0}>0$ . Prove that for any choice of $a_{0}>0$ , the sequence $\{a_{n}\}$  converges. Determine the limit.
2. Let $\Gamma (z)=\int_{0}^{\infty }e^{-t}t^{z-1} \, dt$ . Using the polar coordinate formula, prove the following:

1. $\int_{\mathbb{R}^{d}}^{​}e^{-\pi |x|^{2}} \, dx=1$  when $d=2$ . Deduce from this that the same identity holds for any $d$ .
2. $\left(\int_{0}^{\infty }e^{-\pi r^{2}}r^{d-1} \, dr\right)\sigma (S^{d-1})=1$ , and show that $\sigma (S^{d-1})=\frac{2\pi ^{d/2}}{\Gamma (d/2)}$ .
3. If $B$  is the unit ball, show that $Vol(B)=\frac{\pi ^{d/2}}{\Gamma (d/2+1)}$ .

3. Let $f(x)=\sum_{n=1}^{\infty }\frac{x^{n-1}}{n^{2}(1+x^{n})}$ .

1. Prove that $f(x)$  is continuous for $x\geq 0$ .
2. Evaluate $\int_{0}^{1}f(x) \, dx$ , justifying all steps of your work, and express your answers in terms of values of the function $\zeta (s)=\sum_{n=1}^{\infty }\frac{1}{n^{s}}$ .

4. Suppose $f\geq 0$  on $\mathbb{R}^{d}$ , and let $E_{2^{k}}=\{x:f(x)>2^{k}\}$  and $F_{k}=\{x:2^{k}<f(x)\leq 2^{k+1}\}$ .

1. Show that $f$  is integrable if and only if

$$
\sum_{k=-\infty }^{\infty }2^{k}m(F_{k})<\infty \quad if and only if \quad \sum_{k=-\infty }^{\infty }2^{k}m(E_{2^{k}})<\infty
$$

2. Let $f$  be a nonnegative measurable function on $\mathbb{R}^{d}$  satisfying

$$
m(\{x:f(x)\geq t\})<\frac{1}{1+t^{2}}, \quad t>0.
$$

- Determine those values of $p$ , $1\leq p<\infty$ , for which $f\in L^{p}(\mathbb{R}^{d})$  and find the minimum value of $p$  for which $f$  may fail to be in $L^{p}$ . Give an example.

5. Let $m_{*}$  be the exterior Lebesgue measure. Prove the following:

- A set $E$  in $\mathbb{R}^{d}$  is Caratheodory measurable if and only if $E$  is Lebesgue measurable.
- A set $E$  is Caratheodory measurable if $m_{*}(A)=m_{*}(A\cap E)+m_{*}(A\cap E^{c})$  for any set $A\subset \mathbb{R}^{d}$ . A set $E$  is Lebesgue measurable if for any $\epsilon >0$ , there exists an open set $O$  with $E\subset O$  and $m_{*}(O-E)\leq \epsilon$ .

6. Suppose that $\mu$  and $\nu$  are positive finite measures on $(X\mathscr{,M)}$ , and let $\lambda =\mu +\nu$ . Prove the following:

1. The map $f\mapsto \int_{X}^{​}f \, d\nu$  is a bounded linear functional on $L^{2}(\lambda )$ .
2. There exists a function $g\in L^{2}(\lambda )$  such that

$$
\int_{X}^{​}f \, d\nu =\int_{X}^{​}fg \, d\lambda , \quad equivalently \quad \int_{X}^{​}f(1-g) \, d\nu =\int_{X}^{​}fg \, d\mu .
$$

3. $0\leq <eq>\lambda$ g\leq 1</eq> -a.e., so we may assume $0\leq g\leq 1$ .
4. Let $A=\{x:g(x)<1\}$ , $B=\{x:g(x)=1\}$ , and set $\nu _{a}(E)=\nu (A\cap E)$ , $\nu _{s}(E)=\nu (B\cap E)$ . Then $\nu _{s}⟂\mu$  and $\nu _{a}\ll \mu$ ; in fact $d\nu _{a}=g(1-g)^{-1}\chi _{A} \, d\mu$ .