---
schema: qual/card@1
id: P-TRIV-CA34
kind: problem
title: $\int_0^\infty \frac{dx}{1+x^\alpha}$ by contour integration of $\frac{\log z}{1+z^\alpha}$
classification:
  areas: [complex-analysis]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Complex Analysis, Problem 34, in the deterministic MinerU Flash extraction assets/attachments/Big_List_of_Math_Problems_extracted.md.
- event: source-checked
  by: claude-opus-5
  date: 2026-09-16
  note: Described the Figure 3 contour referenced by Complex Analysis Problem 34, from pages 15 and 18 of the source PDF.
---

::: {.problem}
Solve the integral $\displaystyle\int_0^\infty \frac{1}{1 + x^\alpha}\,dx$ for $\alpha \in \NN$, $\alpha > 1$ by integrating the function $\frac{\log z}{1 + z^\alpha}$ along the contour of figure 3.

Figure 3 of the source shows the contour $C = L_+ \cup C_R \cup L_- \cup \gamma_\epsilon$: $L_+$ runs just above the positive real axis from the small circle $\gamma_\epsilon$ around $0$ out to the large circle $C_R$ of radius $R$ centered at $0$, $C_R$ is traversed counterclockwise, $L_-$ returns just below the positive real axis, and $\gamma_\epsilon$ is traversed clockwise around $0$.
In the source this contour is used with the branch cut on the positive real axis, the radius of $\gamma_\epsilon$ sent to zero and the radius of $C_R$ sent to infinity.
:::

::: {.solution}

Use the branch
$$
\Log z
=
\log|z|+i\arg z,
\qquad
0<\arg z<2\pi,
$$
and define
$$
F(z)
=
\frac{\Log z}{1+z^\alpha}.
$$

::: pf

::: pf-step

The poles of $F$ inside the keyhole contour are
$$
\zeta_k
=
e^{(2k+1)\pi i/\alpha},
\qquad
k=0,1,\ldots,\alpha-1.
$$


::: pf-proof

The poles occur where
$$
z^\alpha=-1.
$$
The displayed $\alpha$ roots have arguments strictly between $0$ and $2\pi$,
so they lie in the slit plane enclosed by the contour.

:::

:::

::: {.pf-step #s1-2}

The residue at $\zeta_k$ is
$$
\operatorname{Res}_{z=\zeta_k}F(z)
=
-\frac{i\theta_k\zeta_k}{\alpha},
\qquad
\theta_k
=
\frac{(2k+1)\pi}{\alpha}.
$$


::: pf-proof

Each pole is simple, and
$$
\Log\zeta_k=i\theta_k.
$$
Thus
$$
\operatorname{Res}_{z=\zeta_k}F(z)
=
\frac{i\theta_k}
{\alpha\zeta_k^{\alpha-1}}.
$$
Since
$$
\zeta_k^\alpha=-1,
$$
one has
$$
\zeta_k^{1-\alpha}
=
-\zeta_k.
$$
Substitution gives the result.

:::

:::

::: {.pf-step #s1-3}

The sum
$$
\sum_{k=0}^{\alpha-1}
\theta_k\zeta_k
$$
equals
$$
-\pi i
\csc\left(\frac\pi\alpha\right).
$$


::: pf-proof

Put
$$
q=e^{2\pi i/\alpha},
\qquad
\zeta_0=e^{\pi i/\alpha}.
$$
Then
$$
\zeta_k=\zeta_0q^k
$$
and
$$
\theta_k
=
\frac\pi\alpha(2k+1).
$$
Hence
$$
\sum_{k=0}^{\alpha-1}
\theta_k\zeta_k
=
\frac\pi\alpha
\zeta_0
\sum_{k=0}^{\alpha-1}
(2k+1)q^k.
$$
Since
$$
\sum_{k=0}^{\alpha-1}q^k=0,
$$
and differentiating this geometric sum gives
$$
\sum_{k=0}^{\alpha-1}kq^k
=
-\frac{\alpha}{1-q},
$$
the preceding sum becomes
$$
-\frac{2\pi\zeta_0}{1-q}.
$$
Finally,
$$
1-q
=
1-\zeta_0^2
=
-2i\zeta_0
\sin\left(\frac\pi\alpha\right),
$$
so
$$
-\frac{2\pi\zeta_0}{1-q}
=
-\pi i
\csc\left(\frac\pi\alpha\right).
$$

:::

:::

::: {.pf-step #s1-4}

Therefore the sum of all residues is
$$
\sum_{k=0}^{\alpha-1}
\operatorname{Res}_{z=\zeta_k}F(z)
=
-\frac\pi\alpha
\csc\left(\frac\pi\alpha\right).
$$


::: pf-proof

By step [](#s1-2){.pf-ref},
$$
\sum_k
\operatorname{Res}_{z=\zeta_k}F
=
-\frac i\alpha
\sum_k\theta_k\zeta_k.
$$
Use step [](#s1-3){.pf-ref} and
$$
(-i)(-i)=-1.
$$

:::

:::

::: {.pf-step #s1-5}

The outer and inner circular-arc contributions tend to zero as
$R\to\infty$ and $\varepsilon\to0^+$.


::: pf-proof

On the outer circle $|z|=R$,
$$
|\Log z|
\leq
\log R+2\pi,
$$
and
$$
|1+z^\alpha|
\geq
R^\alpha-1.
$$
The arc length is $2\pi R$, so the $ML$ estimate gives a bound
$$
\frac{
2\pi R(\log R+2\pi)
}{
R^\alpha-1
}
\longrightarrow0
$$
because $\alpha>1$.

On the inner circle $|z|=\varepsilon$,
$$
|\Log z|
\leq
|\log\varepsilon|+2\pi,
$$
and
$$
|1+z^\alpha|
\geq
1-\varepsilon^\alpha.
$$
The arc length is $2\pi\varepsilon$, so the integral is bounded by
$$
\frac{
2\pi\varepsilon
(|\log\varepsilon|+2\pi)
}{
1-\varepsilon^\alpha
},
$$
which tends to $0$ because
$$
\varepsilon|\log\varepsilon|
\longrightarrow0.
$$

:::

:::

::: {.pf-step #s1-6}

If
$$
J_\alpha
=
\int_0^\infty
\frac{dx}{1+x^\alpha},
$$
then the two ray contributions tend to
$$
-2\pi i J_\alpha.
$$


::: pf-proof

On the upper side of the positive real axis, the branch has
$$
\Log x=\log x,
$$
and the contour runs from $\varepsilon$ to $R$. Hence the contribution is
$$
\int_\varepsilon^R
\frac{\log x}{1+x^\alpha}
\,dx.
$$

On the lower side, the contour returns from $R$ to $\varepsilon$ and
$$
\Log x
=
\log x+2\pi i.
$$
Thus this contribution is
$$
-\int_\varepsilon^R
\frac{\log x+2\pi i}{1+x^\alpha}
\,dx.
$$
Adding the two ray integrals cancels the logarithmic terms and leaves
$$
-2\pi i
\int_\varepsilon^R
\frac{dx}{1+x^\alpha}.
$$
Let
$$
R\to\infty,
\qquad
\varepsilon\to0^+.
$$

:::

:::

::: {.pf-step #s1-7}

By the residue theorem,
$$
-2\pi i J_\alpha
=
2\pi i
\left[
-\frac\pi\alpha
\csc\left(\frac\pi\alpha\right)
\right].
$$


::: pf-proof

By step [](#s1-5){.pf-ref}, only the two ray contributions survive in the limit. Step
[](#s1-6){.pf-ref} gives their value, while the residue theorem and step [](#s1-4){.pf-ref} give the
right-hand side.

:::

:::

::: {.pf-step #s1-8}

Therefore
$$
\boxed{
\int_0^\infty
\frac{dx}{1+x^\alpha}
=
\frac\pi\alpha
\csc\left(\frac\pi\alpha\right)
}.
$$


::: pf-proof

Cancel the common factor $-2\pi i$ in step [](#s1-7){.pf-ref}.

:::

:::

::: pf-qed

Step [](#s1-8){.pf-ref} is the required value.

:::

:::

:::
