---
schema: qual/card@1
id: E-SS6.EX-11
kind: problem
title: The Fourier transform of $e^{az}e^{-e^z}$ is $\Gamma(a-2\pi i\xi)$
classification:
  areas:
  - complex-analysis
  topics:
  - Fourier Transform
  - Gamma Function
relations: []
review: draft
audit:
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-11
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-11
  note: Repaired a transcription defect in the exercise statement before solving.
- event: solution-reviewed
  by: claude
  date: 2026-11-18
  note: >-
    Structured into Lamport steps from the card's own prose. Checked: the integrand has modulus
    e^{ax}e^{-e^x}, independent of xi and integrable over the line for a > 0 (bounded by 1 on
    x <= 0), so the transform is defined; t = e^x with dx = dt/t and t^{a-2 pi i xi} = e^{(a-2 pi i
    xi)x} turns it into the Gamma integral at s = a - 2 pi i xi, whose real part is a > 0 as the
    Gamma definition requires; and |f(x+iy)| = e^{ax}e^{-e^x cos y} gives the printed decay on
    |y| <= pi/2 - delta, together with the reason the strip cannot be widened. The card already
    carries the remark recording that the source prints the strip |y| < pi and the answer
    Gamma(a + i xi), neither of which is right for the book's convention; that remark is left as
    it stands, and the audit records that the statement was not changed in this pass.
---

::: {.exercise}
Let $f(z) = e^{az} e^{-e^z}$ where $a > 0$. Observe that in the strip $\{x + iy : \abs{y} < \pi/2\}$ the function $f(x + iy)$ is exponentially decreasing as $\abs{x}$ tends to infinity. Prove that
$$
\hat{f}(\xi) = \Gamma(a - 2\pi i\xi), \quad \text{for all } \xi \in \RR.
$$
:::

::: {.remark}
The source prints the strip $\abs{y} < \pi$ and the answer $\Gamma(a + i\xi)$. Since $\abs{f(x+iy)} = e^{ax}e^{-e^x\cos y}$ grows as $x \to \infty$ when $\cos y < 0$, the decay holds only for $\abs{y} < \pi/2$. With the book's convention $\hat f(\xi) = \int f(x) e^{-2\pi i x\xi}\,dx$, the transform is $\Gamma(a - 2\pi i\xi)$; $\Gamma(a + i\xi)$ is the transform for the kernel $e^{ix\xi}$.
:::

::: {.solution}
With the book's convention $\widehat f(\xi)=\int f(x)e^{-2\pi ix\xi}\dx$ the substitution $t=e^x$ turns the integral into the definition of the Gamma function at $a-2\pi i\xi$, whose real part is $a>0$; the decay on the strip is the printed observation and is proved in its own step. The argument is this card's own; no retained solution set covers the exercises of Stein--Shakarchi. The statement's printed constants differ from the book's, and the remark above records why.

::: pf

::: {.pf-step #transform}
With $f(x)=e^{ax}e^{-e^x}$ and $a>0$, $\displaystyle\widehat f(\xi)=\int_{-\infty}^{\infty}e^{(a-2\pi i\xi)x}e^{-e^x}\dx$, the integral converging absolutely for every $\xi\in\RR$.

::: pf-proof
By the convention $\widehat f(\xi)=\int f(x)e^{-2\pi ix\xi}\dx$ and $e^{ax}e^{-2\pi ix\xi}=e^{(a-2\pi i\xi)x}$. The modulus of the integrand is $e^{ax}e^{-e^x}$, independent of $\xi$: for $x\le0$ one has $e^{-e^x}\le1$ and $e^{ax}\le1$, so the integrand is bounded by $1$ there, and for $x\ge0$ one has $e^x\ge x$ hence $e^{-e^x}\le e^{-x}$ and $e^{ax}e^{-e^x}\le e^{(a-1)x}$, which is integrable at $+\infty$ because $e^{-e^x}$ beats every exponential: $e^{ax}e^{-e^x}\to0$ superexponentially. So the integral converges absolutely, and uniformly in $\xi$.
:::

:::


::: {.pf-step #substitution}
With $t=e^x$, $\displaystyle\widehat f(\xi)=\int_0^\infty t^{a-2\pi i\xi-1}e^{-t}\dt$.

::: pf-proof
The substitution $t=e^x$ is a strictly increasing diffeomorphism of $\RR$ onto $(0,\infty)$ with $\dx=\dt/t$, and $e^{(a-2\pi i\xi)x}=t^{a-2\pi i\xi}$ because $x=\log t$. Hence
$$
e^{(a-2\pi i\xi)x}e^{-e^x}\dx=t^{a-2\pi i\xi}e^{-t}\,\frac{\dt}{t}=t^{a-2\pi i\xi-1}e^{-t}\dt,
$$
and the integral is absolutely convergent on both sides by step [](#transform){.pf-ref}, so the substitution is legitimate.
:::

:::


::: {.pf-step #gamma}
$\displaystyle\int_0^\infty t^{a-2\pi i\xi-1}e^{-t}\dt=\Gamma(a-2\pi i\xi)$.

::: pf-proof
The Gamma function is defined on the half-plane $\Re s>0$ by $\Gamma(s)=\int_0^\infty t^{s-1}e^{-t}\dt$. Here $s=a-2\pi i\xi$ satisfies $\Re s=a>0$ by the hypothesis $a>0$, so the defining integral converges and equals $\Gamma(s)$; the integral of step [](#substitution){.pf-ref} is that one with $s=a-2\pi i\xi$.
:::

:::


::: {.pf-step #decay}
On every closed substrip $\abs y\le\frac\pi2-\delta$, $0<\delta<\frac\pi2$, the function $\abs{f(x+iy)}$ decays exponentially as $x\to-\infty$ and superexponentially as $x\to+\infty$.

::: pf-proof
$\abs{f(x+iy)}=\abs{e^{a(x+iy)}}\,\abs{e^{-e^{x+iy}}}=e^{ax}e^{-\Re e^{x+iy}}=e^{ax}e^{-e^x\cos y}$, since $\Re(a(x+iy))=ax$ and $\Re e^{x+iy}=e^x\cos y$. As $x\to-\infty$ this equals $e^{ax}$ times a factor tending to $1$, and $a>0$ makes it decrease exponentially. As $x\to+\infty$, $\cos y\ge\cos(\frac\pi2-\delta)=\sin\delta>0$ on the strip, so $e^{-e^x\cos y}\le e^{-e^x\sin\delta}$, which decreases faster than any exponential. This also shows why the strip is $\abs y<\frac\pi2$: where $\cos y<0$ the factor $e^{-e^x\cos y}$ grows superexponentially.
:::

:::


::: {.pf-step #conclusion}
$\widehat f(\xi)=\Gamma(a-2\pi i\xi)$ for all $\xi\in\RR$.

::: pf-proof
Steps [](#transform){.pf-ref}, [](#substitution){.pf-ref} and [](#gamma){.pf-ref} compose to give the identity for every $\xi$, the only hypothesis used being $a>0$; step [](#decay){.pf-ref} supplies the printed observation about the strip and is not needed for the computation itself.
:::

:::

:::
:::
