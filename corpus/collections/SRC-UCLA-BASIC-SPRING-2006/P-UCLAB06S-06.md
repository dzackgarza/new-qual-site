---
schema: qual/card@1
id: P-UCLAB06S-06
kind: problem
title: Compactness of a set of Lipschitz functions with unit $L^2$ norm in $C[0,1]$
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-12
  note: Checked against Problem 6 of the retained UCLA Basic Examination Spring 2006 PDF.
- event: source-checked
  by: claude-opus-5
  date: 2026-09-16
  note: Checked Problem 6 on page 2 of basic-06S.pdf, cleaned the LaTeX, and added an erratum remark that the strict Lipschitz inequality makes W non-closed so (B) fails as stated.
---

::: {.problem}
Let $W$ be the subset of the space $C[0,1]$ of real-valued, continuous functions on $[0,1]$ satisfying the conditions:
\[
|f(x) - f(y)| < |x - y| \qquad \int_0^1 f(x)^2\,dx = 1
\]

(A) Prove that $W$ is uniformly bounded, i.e., there exists $M > 0$ such that $|f(x)| \leq M$ for all $x \in [0,1]$. Hint: Show first that $|f(0)| \leq 2$ for all $f \in W$.

(B) Prove that $W$ is a compact subset of $C[0,1]$ under the sup norm $\|f\|_\infty = \sup_{x \in [0,1]} |f(x)|$.
:::

::: {.remark}
Erratum: with the strict inequality of the source, read for $x \neq y$ (for $x = y$ it would make $W$ empty), part (B) is false because $W$ is not closed. Let $c = \frac{-1 + \sqrt{11/3}}{2}$, so that $g(x) = x + c$ satisfies $\int_0^1 g^2 = \frac13 + c + c^2 = 1$. For $n \ge 2$ choose $c_n$ with $\int_0^1 \bigl((1 - \frac1n)x + c_n\bigr)^2\,dx = 1$ and $c_n \to c$, and put $f_n(x) = (1 - \frac1n)x + c_n$. Then $|f_n(x) - f_n(y)| = (1 - \frac1n)|x - y| < |x - y|$ for $x \neq y$, so $f_n \in W$, and $f_n \to g$ uniformly, but $|g(1) - g(0)| = 1 = |1 - 0|$, so $g \notin W$. Part (B) holds when the condition is $|f(x) - f(y)| \le |x - y|$ for all $x, y \in [0,1]$: that set is closed, and it is uniformly bounded by (A) and equicontinuous, hence compact by the Arzelà–Ascoli theorem.
:::
