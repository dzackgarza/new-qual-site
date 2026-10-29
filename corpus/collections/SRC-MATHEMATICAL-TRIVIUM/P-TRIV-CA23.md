---
schema: qual/card@1
id: P-TRIV-CA23
kind: problem
title: $\int_0^\infty \frac{\log x}{1+x^\alpha}\,dx$ by a wedge contour
classification:
  areas: [complex-analysis]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Complex Analysis, Problem 23, in the deterministic MinerU Flash extraction assets/attachments/Big_List_of_Math_Problems_extracted.md.
- event: source-checked
  by: claude-opus-5
  date: 2026-09-16
  note: Stated problem 34 and the Figure 3 contour referenced by the hint, against Complex Analysis Problems 23 and 34 on pages 15-18 of the source PDF.
---

::: {.problem}
Compute $\displaystyle\int_0^\infty \frac{\log x}{1 + x^\alpha}\,\mathrm{d}x$ for $\alpha \in \NN$, $\alpha > 1$ (**hint:** solve problem 34 first.
Now, as a contour, use a circular wegde of the complex plane that makes a $2\pi/\alpha$ angle with the positive real axis);

Problem 34 of the source reads: Solve the integral $\int_0^\infty \frac{1}{1 + x^\alpha}\,dx$ for $\alpha \in \NN$, $\alpha > 1$ by integrating the function $\frac{\log z}{1 + z^\alpha}$ along the contour of figure 3.

Figure 3 of the source shows the contour $C = L_+ \cup C_R \cup L_- \cup \gamma_\epsilon$: $L_+$ runs just above the positive real axis from the small circle $\gamma_\epsilon$ around $0$ out to the large circle $C_R$ of radius $R$ centered at $0$, $C_R$ is traversed counterclockwise, $L_-$ returns just below the positive real axis, and $\gamma_\epsilon$ is traversed clockwise around $0$.
:::

::: {.solution}

Set
$$
\theta=\frac{2\pi}{\alpha},
\qquad
t=\frac{\pi}{\alpha},
\qquad
\zeta=e^{it}.
$$
Thus
$$
\theta=2t,
\qquad
\zeta^2=e^{i\theta},
\qquad
\zeta^\alpha=-1.
$$

::: pf

::: {.pf-step #s1-1}

In the sector
$$
0<\arg z<\theta,
$$
the function
$$
\frac1{1+z^\alpha}
$$
has exactly one pole, namely
$$
z=\zeta=e^{i\pi/\alpha}.
$$


::: pf-proof

The poles are the roots of
$$
z^\alpha=-1,
$$
namely
$$
z_k=e^{(2k+1)\pi i/\alpha}.
$$
Only the root with argument $\pi/\alpha=t$ lies strictly between $0$ and
$2\pi/\alpha=2t$.

:::

:::

::: {.pf-step #s1-2}

The residue at $\zeta$ is
$$
\operatorname{Res}_{z=\zeta}
\frac1{1+z^\alpha}
=
-\frac{\zeta}{\alpha}.
$$


::: pf-proof

The pole is simple, so
$$
\operatorname{Res}_{z=\zeta}
\frac1{1+z^\alpha}
=
\frac1{\alpha\zeta^{\alpha-1}}.
$$
Since
$$
\zeta^\alpha=-1,
$$
one has
$$
\zeta^{1-\alpha}
=
-\zeta.
$$
Hence the residue is $-\zeta/\alpha$.

:::

:::

::: {.pf-step #s1-3}

Let $C_{\varepsilon,R}$ be the positively oriented boundary of the
annular sector
$$
\varepsilon\leq|z|\leq R,
\qquad
0\leq\arg z\leq\theta,
$$
with $0<\varepsilon<1<R$. Then
$$
\int_{C_{\varepsilon,R}}
\frac{dz}{1+z^\alpha}
=
-\frac{2\pi i\zeta}{\alpha}.
$$


::: pf-proof

By steps [](#s1-1){.pf-ref} through [](#s1-2){.pf-ref}, the contour encloses exactly the simple pole $\zeta$.
The residue theorem gives
$$
2\pi i
\left(-\frac{\zeta}{\alpha}\right).
$$

:::

:::

::: {.pf-step #s1-4}

The two circular-arc integrals in step [](#s1-3){.pf-ref} tend to $0$ as
$R\to\infty$ and $\varepsilon\to0^+$.


::: pf-proof

On $|z|=R$,
$$
|1+z^\alpha|
\geq
R^\alpha-1.
$$
The outer arc has length $\theta R$, so its integral has absolute value at
most
$$
\frac{\theta R}{R^\alpha-1}
\longrightarrow0
$$
because $\alpha>1$.

On $|z|=\varepsilon$,
$$
|1+z^\alpha|
\geq
1-\varepsilon^\alpha.
$$
The inner arc has length $\theta\varepsilon$, so its integral has absolute
value at most
$$
\frac{\theta\varepsilon}{1-\varepsilon^\alpha}
\longrightarrow0.
$$

:::

:::

::: {.pf-step #s1-5}

If
$$
J_\alpha
=
\int_0^\infty\frac{dx}{1+x^\alpha},
$$
then
$$
(1-e^{i\theta})J_\alpha
=
-\frac{2\pi i\zeta}{\alpha}.
$$


::: pf-proof

Along the lower ray $z=x$,
$$
dz=dx,
$$
so the limiting ray integral is $J_\alpha$.

Along the upper ray $z=xe^{i\theta}$, traversed from $R$ back to
$\varepsilon$,
$$
dz=e^{i\theta}dx
$$
and
$$
z^\alpha
=
x^\alpha e^{i\alpha\theta}
=
x^\alpha e^{2\pi i}
=
x^\alpha.
$$
Thus the limiting upper-ray contribution is
$$
-e^{i\theta}J_\alpha.
$$
Let $R\to\infty$ and $\varepsilon\to0$ in step [](#s1-3){.pf-ref} and use step [](#s1-4){.pf-ref}.

:::

:::

::: {.pf-step #s1-6}

One has
$$
\boxed{
J_\alpha
=
\frac{\pi}{\alpha}
\csc\left(\frac\pi\alpha\right).
}
$$


::: pf-proof

Since
$$
1-e^{i\theta}
=
1-\zeta^2
=
-2i\zeta\sin t,
$$
step [](#s1-5){.pf-ref} becomes
$$
-2i\zeta\sin t\,J_\alpha
=
-\frac{2\pi i\zeta}{\alpha}.
$$
Cancel the nonzero factor $-2i\zeta$ to obtain
$$
J_\alpha
=
\frac{\pi}{\alpha\sin t}.
$$
Substitute $t=\pi/\alpha$.

:::

:::

::: {.pf-step #s1-7}

On the sector
$$
0\leq\arg z\leq\theta,
$$
use the branch
$$
\Log z=\log|z|+i\arg z.
$$
Then
$$
\operatorname{Res}_{z=\zeta}
\frac{\Log z}{1+z^\alpha}
=
-\frac{i\pi\zeta}{\alpha^2}.
$$


::: pf-proof

At
$$
\zeta=e^{i\pi/\alpha},
$$
the chosen branch gives
$$
\Log\zeta
=
i\frac\pi\alpha.
$$
Using the simple-pole residue formula,
$$
\operatorname{Res}_{z=\zeta}
\frac{\Log z}{1+z^\alpha}
=
\frac{\Log\zeta}{\alpha\zeta^{\alpha-1}}.
$$
By step [](#s1-2){.pf-ref},
$$
\frac1{\alpha\zeta^{\alpha-1}}
=
-\frac\zeta\alpha.
$$
Hence the residue is
$$
-\frac{i\pi\zeta}{\alpha^2}.
$$

:::

:::

::: {.pf-step #s1-8}

The residue theorem gives
$$
\int_{C_{\varepsilon,R}}
\frac{\Log z}{1+z^\alpha}\,dz
=
\frac{2\pi^2\zeta}{\alpha^2}.
$$


::: pf-proof

By step [](#s1-7){.pf-ref},
$$
2\pi i
\left(
-\frac{i\pi\zeta}{\alpha^2}
\right)
=
\frac{2\pi^2\zeta}{\alpha^2}.
$$

:::

:::

::: {.pf-step #s1-9}

The two circular-arc integrals in step [](#s1-8){.pf-ref} tend to $0$ as
$R\to\infty$ and $\varepsilon\to0^+$.


::: pf-proof

On the outer arc,
$$
|\Log z|
\leq
\log R+\theta.
$$
Using the same denominator bound as in step [](#s1-4){.pf-ref}, the $ML$ estimate gives
$$
\left|
\int_{|z|=R}
\frac{\Log z}{1+z^\alpha}\,dz
\right|
\leq
\frac{\theta R(\log R+\theta)}
{R^\alpha-1}
\longrightarrow0,
$$
because $\alpha>1$.

On the inner arc,
$$
|\Log z|
\leq
|\log\varepsilon|+\theta.
$$
Hence
$$
\left|
\int_{|z|=\varepsilon}
\frac{\Log z}{1+z^\alpha}\,dz
\right|
\leq
\frac{
\theta\varepsilon
(|\log\varepsilon|+\theta)
}{
1-\varepsilon^\alpha
}.
$$
Since
$$
\varepsilon|\log\varepsilon|
\longrightarrow0,
$$
this bound tends to $0$.

:::

:::

::: {.pf-step #s1-10}

Let
$$
I_\alpha
=
\int_0^\infty
\frac{\log x}{1+x^\alpha}\,dx.
$$
Then
$$
(1-e^{i\theta})I_\alpha
-
i\theta e^{i\theta}J_\alpha
=
\frac{2\pi^2\zeta}{\alpha^2}.
$$


::: pf-proof

Along the lower ray,
$$
\Log x=\log x,
$$
so the contribution tends to $I_\alpha$.

Along the upper ray,
$$
z=xe^{i\theta},
\qquad
\Log z=\log x+i\theta,
\qquad
dz=e^{i\theta}dx,
$$
and the path is traversed from $R$ to $\varepsilon$. Since
$$
z^\alpha=x^\alpha,
$$
the upper-ray contribution tends to
$$
-e^{i\theta}
\int_0^\infty
\frac{\log x+i\theta}{1+x^\alpha}\,dx
$$
which equals
$$
-e^{i\theta}I_\alpha
-
i\theta e^{i\theta}J_\alpha.
$$
Now let $R\to\infty$ and $\varepsilon\to0$ in step [](#s1-8){.pf-ref} and use
step [](#s1-9){.pf-ref}.

:::

:::

::: {.pf-step #s1-11}

One has
$$
\boxed{
I_\alpha
=
-\frac{\pi^2}{\alpha^2}
\csc\left(\frac\pi\alpha\right)
\cot\left(\frac\pi\alpha\right).
}
$$


::: pf-proof

Recall
$$
t=\frac\pi\alpha,
\qquad
\theta=2t,
\qquad
e^{i\theta}=\zeta^2,
$$
and by step [](#s1-6){.pf-ref},
$$
J_\alpha=t\csc t.
$$
Also,
$$
1-e^{i\theta}
=
-2i\zeta\sin t.
$$
Substitute these into step [](#s1-10){.pf-ref}:
$$
-2i\zeta\sin t\,I_\alpha
-
2it\zeta^2
\bigl(t\csc t\bigr)
=
2t^2\zeta.
$$
Divide by $-2i\zeta$:
$$
\sin t\,I_\alpha
+
t^2\zeta\csc t
=
it^2.
$$
Since
$$
\zeta=e^{it}=\cos t+i\sin t,
$$
one has
$$
\zeta\csc t
=
\cot t+i.
$$
Therefore
$$
\sin t\,I_\alpha
+
t^2(\cot t+i)
=
it^2,
$$
so
$$
I_\alpha
=
-t^2\frac{\cot t}{\sin t}
=
-t^2\csc t\cot t.
$$
Substitute
$$
t=\frac\pi\alpha.
$$

:::

:::

::: pf-qed

Step [](#s1-11){.pf-ref} is the required value of the integral.

:::

:::

:::
