---
schema: qual/card@1
id: P-BKS19-3A
kind: problem
title: Sup-norm bound $\max\abs{f}\le\frac18\max\abs{f''}$ with zero boundary values
classification:
  areas:
  - prelim
  topics:
  - Real Analysis
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-13
  note: Checked against the vendored UC Berkeley Spring 2019 Graduate Preliminary Examination.
- event: source-checked
  by: chatgpt
  date: 2026-10-02
  note: Independently reviewed the supplied Berkeley Spring 2019 maximum-point and integration-by-parts argument. The proof and equality example are correct; the solution below makes the zero-function and interior-maximum cases explicit.
- event: solution-written
  by: chatgpt
  date: 2026-10-02
- event: solution-reviewed
  by: chatgpt
  date: 2026-10-02
  note: Verified the symmetry reduction, critical-point condition, integration-by-parts estimate, and equality for $f(x)=x(x-1)/2$.
---

::: {.problem}
Let $f$ be a twice continuously differentiable function on $[0,1]$ such that $f(0)=f(1)=0$.
Prove that
$$
\max_{x\in[0,1]}\abs{f(x)}\le \frac18\max_{x\in[0,1]}\abs{f''(x)},
$$
and find an example where equality holds.
:::

::: {.solution}

Set
$$
M\coloneqq\max_{x\in[0,1]}\abs{f''(x)}.
$$

::: pf

::: {.pf-step #s1-1}

If $f$ is not identically zero, there is a point $\alpha\in(0,1)$ with
$$
\abs{f(\alpha)}=\max_{x\in[0,1]}\abs{f(x)}
$$
and $f'(\alpha)=0$.


::: pf-proof

Continuity gives a point where $\abs{f}$ attains its maximum. Since $f(0)=f(1)=0$ and $f$ is not identically zero, the maximum is positive and cannot occur only at an endpoint; hence it is attained at some $\alpha\in(0,1)$. At such a point either $f$ has a local maximum or a local minimum, so Fermat's theorem gives $f'(\alpha)=0$.

:::

:::

::: {.pf-step #s1-2}

After replacing $f(x)$ by $f(1-x)$ if necessary, the point in step [](#s1-1){.pf-ref} may be chosen with $0<\alpha\leq\frac12$.


::: pf-proof

If $\alpha\leq\frac12$, there is nothing to prove. If $\alpha>\frac12$, define $g(x)=f(1-x)$. Then $g(0)=g(1)=0$, $\max\abs{g}=\max\abs{f}$, and $\max\abs{g''}=\max\abs{f''}$, while $\abs{g(1-\alpha)}=\abs{f(\alpha)}$ and $1-\alpha<\frac12$. Thus the desired estimate for $g$ is equivalent to that for $f$.

:::

:::

::: {.pf-step #s1-3}

One has
$$
\max_{x\in[0,1]}\abs{f(x)}\leq\frac18M.
$$


::: pf-proof

If $f\equiv0$, the inequality is immediate. Otherwise take $\alpha$ as in steps [](#s1-1){.pf-ref} through [](#s1-2){.pf-ref}. Since $f(0)=0$,
$$
f(\alpha)=\int_0^\alpha f'(x)\,dx.
$$
Integration by parts gives
$$
\int_0^\alpha f'(x)\,dx
=
\alpha f'(\alpha)-\int_0^\alpha x f''(x)\,dx
=
-\int_0^\alpha x f''(x)\,dx,
$$
because $f'(\alpha)=0$ by step [](#s1-1){.pf-ref}. Therefore
$$
\max\abs{f}
=\abs{f(\alpha)}
\leq
M\int_0^\alpha x\,dx
=
\frac{M\alpha^2}{2}
\leq
\frac{M}{8},
$$
using $\alpha\leq1/2$.

:::

:::

::: {.pf-step #s1-4}

Equality is attained by
$$
\boxed{f(x)=\frac{x(x-1)}2}.
$$


::: pf-proof

This function satisfies $f(0)=f(1)=0$ and $f''(x)=1$, so
$$
\max_{[0,1]}\abs{f''}=1.
$$
Moreover $f(x)\leq0$ on $[0,1]$, with its minimum at $x=1/2$, where
$$
f\left(\frac12\right)=-\frac18.
$$
Hence $\max\abs{f}=1/8=(1/8)\max\abs{f''}$.

:::

:::

::: pf-qed

Step [](#s1-3){.pf-ref} proves the inequality, and step [](#s1-4){.pf-ref} supplies an equality example.

:::

:::

:::
