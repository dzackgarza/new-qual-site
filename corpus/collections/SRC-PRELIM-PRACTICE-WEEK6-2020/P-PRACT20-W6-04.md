---
schema: qual/card@1
id: P-PRACT20-W6-04
kind: problem
title: Pointwise and uniform convergence of $x^n/(1+x^n)$ on $[0,1]$
classification:
  areas:
  - prelim
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: claude-opus-5
  date: 2026-09-16
  note: Moved choice (C) out of a display into its labelled paragraph and restored the arrows lost from the solution display, checked against Week6_solns.pdf page 2 (Problem 4, which has only choices A-C).
- event: source-checked
  by: claude-opus-5
  date: 2026-09-16
  note: Restored two arrows lost from inline solution formulas and dropped a stray 2, checked against Week6_solns.pdf page 2 (Problem 4).
---

::: {.problem}
Define $f_n(x) = \frac{x^n}{1 + x^n}$ for $x \in [0, 1]$, $n \in \NN$. Which of the following is true?

(A) The sequence $\{f_n\}$ converges pointwise on $[0, 1]$ to a limit function $f$.

(B) The sequence $\{f_n\}$ converges uniformly on $[0, 1]$ to a limit function $f$.

(C) $\displaystyle\lim_{n \to \infty} \int_0^1 f_n(x)\,dx = \int_0^1 \left(\lim_{n \to \infty} f_n(x)\right) dx$
:::

::: {.solution}
At $x = 1$ , we see that $f _ { n } ( 1 ) = 1 / 2$ for all $n \in \mathbb { N }$ so $f _ { n } ( 1 ) \to 1 / 2$. For any $x \in [ 0 , 1 )$ , we have

$$
0 \leq f _ { n } ( x ) = { \frac { x ^ { n } } { 1 + x ^ { n } } } \leq x ^ { n } \to 0 , \quad { \mathrm { ~ a s ~ } } \ n \to \infty .
$$

Thus f converges pointwise to the function

$$
f ( x ) = { \left\{ \begin{array} { l l } { 0 , } & { x \in [ 0 , 1 ) } \\ { 1 / 2 , } & { x = 1 . } \end{array} \right. }
$$

Now each $f _ { n }$ is continuous, but this limit is discontinuous - we conclude that the convergence is not uniform since the uniform limit of continuous functions remains continuous.
However, since the domain is compact and each $f _ { n }$ is bounded by 1 for all $x \in [ 0 , 1 ]$ , the limit of the integrals is the integral of the limit.
More explicitly

$$
0 \leq \int _ { 0 } ^ { 1 } f _ { n } ( x ) d x = \int _ { 0 } ^ { 1 } { \frac { x ^ { n } d x } { 1 + x ^ { n } } } \leq \int _ { 0 } ^ { 1 } x ^ { n } d x = { \frac { 1 } { n + 1 } } \to 0
$$

and $\begin{array} { r } { \int _ { 0 } ^ { 1 } f ( x ) d x = 0 } \end{array}$ so $\begin{array} { r } { \int _ { 0 } ^ { 1 } f _ { n } ( x ) d x \to \int _ { 0 } ^ { 1 } f ( x ) d x } \end{array}$ . Thus we conclude that (A) and (C) are true, while (B) is false.
:::
