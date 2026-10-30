---
schema: qual/card@1
id: P-TRIV-DE26
kind: problem
title: Small-$x$ asymptotics of the modified Bessel function $K_\nu$
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Differential Equations, Problem 26, in the deterministic MinerU Flash extraction assets/attachments/Big_List_of_Math_Problems_extracted.md. Flash contains a leading nonprinting control byte at this source position; the byte was removed from the authored card as a nonsemantic extraction artifact.
---

::: {.problem}
The function $K_\nu(x)$ is the solution of the equation $x^2y'' + xy' - (x^2 + \nu^2)y = 0$ that diverges when $x \to 0$. Find the asymptotic behavior for small $x$ for $\nu \neq 0$. What happens for $\nu = 0$? For the sake of completeness, $K_\nu(x)$ is called modified Bessel function of the second kind.
:::

::: {.solution}

Take $x>0$. Recall that $K_{-\nu}=K_\nu$.

::: pf

::: pf-step

For $\nu\ne0$, the indicial equation at $x=0$ is
$$
r^2-\nu^2=0,
$$
with roots $r=\pm\nu$.


::: pf-proof

Insert a Frobenius leading term $y\sim x^r$ into
$$
x^2y''+xy'-(x^2+\nu^2)y=0.
$$
The terms of lowest order are
$$
\bigl(r(r-1)+r-\nu^2\bigr)x^r
=(r^2-\nu^2)x^r.
$$
Thus the two local powers are $x^\nu$ and $x^{-\nu}$.

:::

:::

::: {.pf-step #s1-2}

If $\nu\ne0$, the divergent branch has leading power $x^{-\abs{\nu}}$, and the standard normalization of $K_\nu$ gives
$$
\boxed{K_\nu(x)\sim 2^{\abs{\nu}-1}\Gamma(\abs{\nu})x^{-\abs{\nu}}}
\qquad(x\to0^+).
$$


::: pf-proof

By $K_{-\nu}=K_\nu$, it suffices to take $\nu>0$. For nonintegral $\nu$,
$$
K_\nu(x)=\frac{\pi}{2\sin(\pi\nu)}\bigl(I_{-\nu}(x)-I_\nu(x)\bigr).
$$
The modified-Bessel series give
$$
I_{-\nu}(x)\sim\frac{(x/2)^{-\nu}}{\Gamma(1-\nu)},
\qquad
I_\nu(x)\sim\frac{(x/2)^\nu}{\Gamma(1+\nu)}.
$$
The first term dominates. Euler's reflection identity
$$
\Gamma(\nu)\Gamma(1-\nu)=\frac\pi{\sin(\pi\nu)}
$$
therefore gives
$$
K_\nu(x)\sim\frac12\Gamma(\nu)(x/2)^{-\nu}
=2^{\nu-1}\Gamma(\nu)x^{-\nu}.
$$
The same leading formula at positive integral $\nu$ follows by continuity in the order.

:::

:::

::: {.pf-step #s1-3}

For $\nu=0$, the two indicial roots coalesce at $r=0$, and the divergent solution is logarithmic rather than a power:
$$
\boxed{K_0(x)\sim-\log(x/2)-\gamma}
\qquad(x\to0^+),
$$
where $\gamma$ is Euler's constant.


::: pf-proof

Use the representation from step [](#s1-2){.pf-ref} and take the limit $\nu\to0$. The expansions
$$
I_\nu(x)=I_0(x)+O(\nu),
\qquad I_0(x)=1+O(x^2),
$$
together with
$$
\Gamma(1+\nu)=1-\gamma\nu+O(\nu^2),
\qquad
(x/2)^\nu=1+\nu\log(x/2)+O(\nu^2)
$$
show that the cancellation of the two coincident power branches leaves the logarithmic term $-\log(x/2)-\gamma$.

:::

:::

::: pf-qed

Steps [](#s1-2){.pf-ref} and [](#s1-3){.pf-ref} give the requested small-$x$ behavior for nonzero and zero order, respectively.

:::

:::

:::
