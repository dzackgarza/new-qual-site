---
schema: qual/card@1
id: P-GREPT-38
kind: problem
title: "Conditions forcing a real function on an interval to be constant"
classification:
  areas: [prelim]
  topics:
  - Mean Value Theorem
  - Constant Functions
relations: []
review: draft
audit:
- event: source-checked
  by: claude-opus-5
  date: 2026-09-16
  note: "Transcribed from Question 38 of the Practice Test (Chapter 9) in assets/attachments/extracted/Cracking_the_GRE_Mathematics_Subject.md (Mistral OCR)."
---

::: {.problem}
Consider the set $X$ of all real-valued functions defined on the interval $[a, b]$, where $a < b$. Which of the following conditions, if true, would ensure that $f \in X$ is constant on $[a, b]$?

I. The inverse of $f$ is a constant function.

II. The composite function $f \circ g$ is constant for every function $g$ in $X$.

III. $\abs{f(x) - f(y)} \leq (x - y)^2$ for every $x$ and $y$ in $[a, b]$.

(A) II only
(B) I and II only
(C) I and III only
(D) II and III only
(E) I, II, and III
:::

::: {.solution}

::: pf

::: {.pf-step #s1-1}

Condition I cannot hold for a function on the nondegenerate interval
$[a,b]$; consequently, as a formal implication it is vacuously sufficient.


::: pf-proof

If $f$ has an inverse function, then
$$
f^{-1}(f(x))=x
$$
for every $x\in[a,b]$. Since $a<b$, the inverse takes the distinct values
$a$ and $b$ at $f(a)$ and $f(b)$ respectively, so it cannot be constant.
Thus no $f\in X$ satisfies condition I. Therefore the implication
"if condition I holds, then $f$ is constant" is formally true only
vacuously.

:::

:::

::: {.pf-step #s1-2}

Condition II is not literally well-typed for every $g\in X$, but under
the intended composable-map reading it forces $f$ to be constant.


::: pf-proof

An arbitrary $g\in X$ is merely a real-valued function on $[a,b]$ and need
not take its values in $[a,b]$, so $f\circ g$ need not be defined. Under the
intended reading in which the condition ranges over maps for which the
composition is defined, take $g$ to be the identity function on $[a,b]$.
Then $g\in X$ and
$$
f\circ g=f.
$$
If $f\circ g$ is constant for every such $g$, it is constant for this choice,
so $f$ itself is constant.

:::

:::

::: {.pf-step #s1-3}

Condition III forces $f$ to be constant.


::: pf-proof

Fix $x<y$ in $[a,b]$ and, for an integer $n\ge1$, set
$$
x_j=x+\frac{j}{n}(y-x),
\qquad 0\le j\le n.
$$
By the triangle inequality and condition III,
$$
\begin{aligned}
\abs{f(y)-f(x)}
&\le\sum_{j=1}^n\abs{f(x_j)-f(x_{j-1})}\\
&\le n\left(\frac{y-x}{n}\right)^2
=\frac{(y-x)^2}{n}.
\end{aligned}
$$
Letting $n\to\infty$ gives $\abs{f(y)-f(x)}=0$. Hence $f(y)=f(x)$ for every
$x,y\in[a,b]$, so $f$ is constant.

:::

:::

::: {.pf-step #s1-4}

Therefore the multiple-choice question is not well-posed under a
literal formal reading:
$$
\boxed{\text{the literal statement determines no single listed choice}}.
$$


::: pf-proof

Step [](#s1-1){.pf-ref} shows that condition I is impossible and hence vacuously sufficient
when read as an implication. Step [](#s1-2){.pf-ref} shows that condition II is not defined
under the stated quantifier over all $g\in X$. Thus the literal formulation
does not determine one of the listed subsets of I--III, although step [](#s1-3){.pf-ref}
proves that condition III is genuinely sufficient.

:::

:::

::: pf-qed

Step [](#s1-4){.pf-ref} gives the conclusion supported by the statement as written.

:::

:::

:::

::: {.remark}
The source intends answer (D): it discards the impossible condition I, reads
condition II as ranging over composable maps, and counts II and III as the
substantive constancy criteria. Under that intended reading, steps [](#s1-2){.pf-ref} through [](#s1-3){.pf-ref}
prove exactly II and III.
:::
