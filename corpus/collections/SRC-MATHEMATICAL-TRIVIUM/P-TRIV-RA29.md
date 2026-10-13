---
schema: qual/card@1
id: P-TRIV-RA29
kind: problem
title: Convergence of the pendulum period integral at the turning point
classification:
  areas: [real-analysis]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Real Analysis, Problem 29, in the deterministic MinerU Flash extraction assets/attachments/Big_List_of_Math_Problems_extracted.md. Flash drops the arrow in the phrase describing the limit as $\phi$ approaches $\phi_0$; the card retains the extracted text rather than inventing typography.
- event: source-checked
  by: claude-opus-5
  date: 2026-09-16
  note: Restored the lost arrow in phi to phi_0 against Real Analysis Problem 29 on page 10 of the source PDF.
---

::: {.problem}
Is the integral $\displaystyle\int_0^{\phi} \frac{d\psi}{\sqrt{\sin^2\frac{\phi_0}{2} - \sin^2\frac{\psi}{2}}}$ convergent as $\phi \to \phi_0$?
:::

::: {.remark}
For the pendulum regime $0<\phi_0<\pi$, the improper limit is convergent.
At the limiting amplitude $\phi_0=\pi$, the endpoint singularity becomes
logarithmic and the integral diverges.
:::

::: {.solution}
Assume first that
$$
0<\phi_0<\pi,
$$
and set
$$
k=\sin\frac{\phi_0}{2}.
$$
Then
$$
0<k<1.
$$

<1>1. Use the substitution
$$
u=
\frac{\sin(\psi/2)}{k}.
$$

::: {.proof}
For
$$
0\leq\psi\leq\phi_0<\pi,
$$
the function $\sin(\psi/2)$ is increasing, so the substitution is valid.
:::

<1>2. Under this substitution,
$$
d\psi
=
\frac{2k\,du}{\sqrt{1-k^2u^2}},
$$
and
$$
\sqrt{
k^2-sin^2\frac\psi2
}
=
k\sqrt{1-u^2}.
$$

::: {.proof}
Differentiating
$$
ku=\sin\frac\psi2
$$
gives
$$
k\,du
=
\frac12\cos\frac\psi2\,d\psi.
$$
Since
$$
\cos\frac\psi2
=
\sqrt{1-\sin^2\frac\psi2}
=
\sqrt{1-k^2u^2},
$$
the first formula follows. The second is immediate from the definition of
$u$.
:::

<1>3. Therefore
$$
\int_0^{\phi}
\frac{d\psi}{
\sqrt{
\sin^2(\phi_0/2)-\sin^2(\psi/2)
}
}
=
2
\int_0^{u(\phi)}
\frac{du}{
\sqrt{1-u^2}
\sqrt{1-k^2u^2}
}.
$$

::: {.proof}
Substitute the two identities from step <1>2. The factors of $k$ cancel.
:::

<1>4. As $\phi\to\phi_0^-$,
$$
u(\phi)\to1^-.
$$

::: {.proof}
By definition,
$$
u(\phi)
=
\frac{\sin(\phi/2)}{\sin(\phi_0/2)}.
$$
Continuity of sine gives the limit.
:::

<1>5. Near $u=1$,
$$
\frac{1}{
\sqrt{1-u^2}
\sqrt{1-k^2u^2}
}
=
O\left((1-u)^{-1/2}\right).
$$

::: {.proof}
Since $k<1$,
$$
1-k^2u^2
\longrightarrow
1-k^2
>0
$$
as $u\to1^-$. Thus the second square-root factor stays bounded away from
$0$. Also
$$
1-u^2
=(1-u)(1+u)
\asymp
2(1-u).
$$
Hence the only singular factor has order $(1-u)^{-1/2}$.
:::

<1>6. The limiting integral is convergent for
$$
0<\phi_0<\pi.
$$

::: {.proof}
By step <1>5, the endpoint behavior is dominated by a constant multiple of
$$
(1-u)^{-1/2},
$$
whose integral near $u=1$ is finite. Therefore the improper integral in step
<1>3 converges as the upper endpoint tends to $1$.
:::

<1>7. If
$$
\phi_0=\pi,
$$
the integral diverges logarithmically.

::: {.proof}
Now $k=1$, so the integrand in step <1>3 becomes
$$
\frac{2}{1-u^2}.
$$
Near $u=1$,
$$
\frac{2}{1-u^2}
\sim
\frac{1}{1-u},
$$
whose integral diverges logarithmically.
:::

<1>8. Hence
$$
\boxed{
\text{the integral converges as }\phi\to\phi_0
\text{ for }0<\phi_0<\pi.
}
$$

::: {.proof}
This is step <1>6; step <1>7 records the endpoint exception $\phi_0=\pi$.
:::

<1>9. Q.E.D.

::: {.proof}
Steps <1>6--<1>8 give the complete convergence statement in the physically
relevant range.
:::
:::
