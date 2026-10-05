---
schema: qual/card@1
id: P-WESTOP06-B4
kind: problem
title: Constant paths are left and right identities for path multiplication
classification: {areas: [topology], topics: []}
relations: []
review: draft
audit:
- {event: source-checked, by: gpt-5.6-sol, date: 2026-09-14}
---

::: {.problem}
Let $c_x:I\to X$ be the constant path at $x$, and let $f$ be a path from $x_0$ to $x_1$. Construct explicit path homotopies, algebraically and with diagrams, proving
\[
[f]*[c_{x_1}]=[f]
\qquad\text{and}\qquad
[c_{x_0}]*[f]=[f].
\]
:::

::: {.solution}
Use the standard concatenation convention
\[
(a*b)(t)=
\begin{cases}
a(2t),&0\le t\le\tfrac12,\\
b(2t-1),&\tfrac12\le t\le1.
\end{cases}
\]

<1>1. The path \(f*c_{x_1}\) is the reparametrization
\[
(f*c_{x_1})(t)=f(\lambda_0(t)),
\qquad
\lambda_0(t)=\min\{2t,1\}.
\]

::: {.proof}
If \(0\le t\le\tfrac12\), then \(\lambda_0(t)=2t\), so \(f(\lambda_0(t))=f(2t)\). If \(\tfrac12\le t\le1\), then \(\lambda_0(t)=1\), so
\[
f(\lambda_0(t))=f(1)=x_1=c_{x_1}(2t-1).
\]
These are exactly the two pieces of \(f*c_{x_1}\).
:::

<1>2. The maps
\[
\lambda_s(t)=(1-s)\min\{2t,1\}+st
\]
give a path homotopy
\[
H_R(t,s)=f(\lambda_s(t))
\]
from \(f*c_{x_1}\) to \(f\), relative to the endpoints.

::: {.proof}
The function \((t,s)\mapsto\lambda_s(t)\) is continuous and takes values in \(I\), so \(H_R\) is continuous. By step <1>1,
\[
H_R(t,0)=(f*c_{x_1})(t),
\qquad
H_R(t,1)=f(t).
\]
For every \(s\),
\[
\lambda_s(0)=0,\qquad \lambda_s(1)=1,
\]
so
\[
H_R(0,s)=x_0,\qquad H_R(1,s)=x_1.
\]
Thus \(H_R\) is a path homotopy relative to endpoints.

The reparametrization diagram is
\[
\begin{array}{ccc}
I&\xrightarrow{\ \lambda_s\ }&I\\
&\searrow{\scriptstyle H_R(-,s)}&\downarrow{\scriptstyle f}\\
&&X.
\end{array}
\]
At \(s=0\), the first half of \(I\) is stretched across all of \(I\) and the second half is collapsed to \(1\); at \(s=1\), \(\lambda_1=\operatorname{id}_I\).
:::

<1>3. Hence
\[
\boxed{[f]*[c_{x_1}]=[f].}
\]

::: {.proof}
Step <1>2 gives a path homotopy from \(f*c_{x_1}\) to \(f\), so the two paths determine the same path-homotopy class.
:::

<1>4. The path \(c_{x_0}*f\) is the reparametrization
\[
(c_{x_0}*f)(t)=f(\mu_0(t)),
\qquad
\mu_0(t)=\max\{2t-1,0\}.
\]

::: {.proof}
If \(0\le t\le\tfrac12\), then \(\mu_0(t)=0\), so
\[
f(\mu_0(t))=f(0)=x_0=c_{x_0}(2t).
\]
If \(\tfrac12\le t\le1\), then \(\mu_0(t)=2t-1\), so \(f(\mu_0(t))=f(2t-1)\). These are exactly the two pieces of \(c_{x_0}*f\).
:::

<1>5. The maps
\[
\mu_s(t)=(1-s)\max\{2t-1,0\}+st
\]
give a path homotopy
\[
H_L(t,s)=f(\mu_s(t))
\]
from \(c_{x_0}*f\) to \(f\), relative to the endpoints.

::: {.proof}
The function \((t,s)\mapsto\mu_s(t)\) is continuous and takes values in \(I\), so \(H_L\) is continuous. By step <1>4,
\[
H_L(t,0)=(c_{x_0}*f)(t),
\qquad
H_L(t,1)=f(t).
\]
For every \(s\),
\[
\mu_s(0)=0,\qquad \mu_s(1)=1,
\]
so both endpoints stay fixed.

The corresponding parameter diagram is
\[
\begin{array}{ccc}
I&\xrightarrow{\ \mu_s\ }&I\\
&\searrow{\scriptstyle H_L(-,s)}&\downarrow{\scriptstyle f}\\
&&X.
\end{array}
\]
At \(s=0\), the first half of \(I\) is collapsed to \(0\) and the second half is stretched across all of \(I\); at \(s=1\), \(\mu_1=\operatorname{id}_I\).
:::

<1>6. Hence
\[
\boxed{[c_{x_0}]*[f]=[f].}
\]

::: {.proof}
Step <1>5 gives a path homotopy from \(c_{x_0}*f\) to \(f\), so they determine the same path-homotopy class.
:::

<1>7. Q.E.D.

::: {.proof}
Steps <1>3 and <1>6 establish the right- and left-identity laws requested in the problem.
:::
:::
