---
schema: qual/card@1
id: P-6Y3IL
kind: problem
title: "Suppose that $f_j \\in L^2(\\mathbb{R}^d)$, $j = 1, 2, \\ldots$, and $f \\in L^2(\\mathbb{R}^d)$ satisfy $\\lim_{j\\to\\infty} \\int_{\\mathbb{R}^d} f_j g = \\int_{\\mathbb{R}^d} fg$ for all $g \\in L^2(\\mathbb{R}^d)$."
classification:
  areas:
  - real-analysis
  topics:
  - weak-convergence
  - l2
  - hilbert-spaces
relations: []
review: draft
solved: true
---

::: {.problem title="?"}
Suppose that $f_j \in L^2(\mathbb{R}^d)$, $j = 1, 2, \ldots$, and $f \in L^2(\mathbb{R}^d)$ satisfy $$\lim_{j\to\infty} \int_{\mathbb{R}^d} f_j g = \int_{\mathbb{R}^d} fg$$ for all $g \in L^2(\mathbb{R}^d)$.
That is, $f_j$ converges to $f$ weakly in $L^2$.
Suppose that the sequence satisfies the uniform bound $$\sup_{x\in\mathbb{R}^d}(1+|x|)^d|f_j(x)| \le M < \infty. \qquad (A)$$

Show that $\|f_j\|_2 \to \|f\|_2$ and conclude that $\|f_j - f\|_2 \to 0$.
That is $f_j$ converges to $f$ strongly in $L^2(\mathbb{R}^d)$.
Show by example that condition (A) is necessary.
:::
::: {.solution}
> **AI-Generated Solution**

*Honesty note.* As stated, the claim is FALSE: weak convergence in $L^2(\RR^d)$ together with the bound (A) does not imply $\|f_j\|_2 \to \|f\|_2$.
Example: on $\RR$ take $f_j(x) = \sqrt2\,\sin(j\pi x)\,\chi_{[0,1]}(x)$.
Then $f_j \rightharpoonup 0$ weakly (Riemann--Lebesgue: $\int_0^1 \sqrt2\sin(j\pi x)g(x)\,dx \to 0$ for $g\in L^2[0,1]$, and $f_j$ is supported on $[0,1]$), $\sup_x (1+|x|)|f_j(x)| \le 2\sqrt2 < \infty$ satisfies (A) with $M = 2\sqrt2$, yet $\|f_j\|_2 = 1 \not\to 0 = \|0\|_2$.
So the problem needs an extra hypothesis.
We prove the natural corrected statement: assume in addition that $f_j \to f$ pointwise a.e.

<1>1. (Corrected statement) If $f_j \rightharpoonup f$ in $L^2$, $\sup_j\sup_x(1+|x|)^d|f_j(x)| \le M$, and $f_j \to f$ pointwise a.e., then $f_j \to f$ strongly in $L^2$.
Proof: set $g(x) = M(1+|x|)^{-d}$; then $g \in L^2(\RR^d)$ (since $\int (1+|x|)^{-2d}\,dx < \infty$ for $d \ge 1$), and $|f_j| \le g$ a.e. for all $j$.
Pointwise convergence $f_j \to f$ a.e. gives $|f| \le g$ a.e., so $f \in L^2$.
By the dominated convergence theorem (domination $g \in L^2$), $\int|f_j - f|^2 \to 0$, i.e. $\|f_j - f\|_2 \to 0$.
<1>2. (Original claim under (A) alone is false, so the added hypothesis is essential.)
Proof: see the honesty note: without pointwise convergence, (A) only gives domination by $g\in L^2$ and tightness, which do not force strong convergence (the oscillating example $f_j = \sqrt2\sin(j\pi x)\chi_{[0,1]}$). <1>3. (Necessity of (A)-type decay) Without (A), the conclusion fails even with pointwise convergence.
Proof: take $f_j = \chi_{[j,j+1]}$ on $\RR$: $f_j \to 0$ pointwise everywhere, $f_j \rightharpoonup 0$ weakly ($\int f_j g = \int_j^{j+1}g \to 0$ for $g \in L^2$), but $\|f_j\|_2 = 1 \not\to 0$.
Here $\sup_x(1+|x|)|f_j(x)| = j+1 \to \infty$, so (A) fails.
This shows a decay/tightness hypothesis like (A) is necessary (in the corrected statement).
<1>4. Q.E.D.
:::
