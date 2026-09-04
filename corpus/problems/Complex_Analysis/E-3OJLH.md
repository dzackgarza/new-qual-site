---
schema: qual/card@1
id: E-3OJLH
kind: problem
title: The equality case
classification:
  areas:
  - complex-analysis
  topics:
  - Schwarz Lemma
  - Maximum Modulus Principle
relations: []
review: draft
---

::: {.exercise}
Suppose $f:\DD\to \DD$ is holomorphic and $f(0)=0$.
Show that
\[
\abs{f(z)+f(-z)}\le 2\abs z^2
\qquad(z\in\DD).
\]
If equality holds at some $z_0\neq0$, show that
\[
f(z)=\lambda z^2
\]
for some $\abs\lambda=1$.
:::

::: {.solution}
By Schwarz's lemma, $|f(z)|\le |z|$.
Hence
\[
g(z)=
\begin{cases}
f(z)/z,&z\neq0,\\
f'(0),&z=0
\end{cases}
\]
is holomorphic on $\DD$ and satisfies $|g|\le1$.
Set
\[
h(z)=\frac{g(z)-g(-z)}2.
\]
Then $h$ is holomorphic, $h(0)=0$, and $|h(z)|\le1$.
Schwarz's lemma gives $|h(z)|\le|z|$.
Since
\[
f(z)+f(-z)=z\bigl(g(z)-g(-z)\bigr)=2zh(z),
\]
we obtain
\[
|f(z)+f(-z)|\le2|z|^2.
\]

Suppose equality holds at some $z_0\neq0$.
Then $|h(z_0)|=|z_0|$, so the equality case of Schwarz's lemma gives
\[
h(z)=\lambda z,
\qquad |\lambda|=1.
\]
Let
\[
e(z)=\frac{g(z)+g(-z)}2.
\]
Then
\[
g(z)=e(z)+\lambda z,
\qquad
g(-z)=e(z)-\lambda z.
\]
Because $|g(z)|,|g(-z)|\le1$, the parallelogram identity yields
\[
2|e(z)|^2+2|z|^2
=|g(z)|^2+|g(-z)|^2
\le2,
\]
so $|e(z)|\le\sqrt{1-|z|^2}$.
On $|z|=r<1$ this gives $|e(z)|\le\sqrt{1-r^2}$; by the maximum modulus principle the same bound holds on $|z|\le r$.
Letting $r\uparrow1$ shows $e\equiv0$.
Therefore
\[
g(z)=\lambda z,
\qquad
f(z)=zg(z)=\lambda z^2.
\]
Conversely, these maps attain equality for every $z$.
:::
