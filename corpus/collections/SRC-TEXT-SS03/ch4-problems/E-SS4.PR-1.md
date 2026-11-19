---
schema: qual/card@1
id: E-SS4.PR-1
kind: problem
title: "Exponential decay of the Fourier transform gives holomorphy"
classification:
  areas:
  - complex-analysis
  topics:
  - Entire Functions
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-11
  note: Checked against Stein--Shakarchi Chapter 4 source; repaired the statement where needed.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-11
- event: solution-written
  by: claude
  date: 2026-11-19
  note: >-
    Restructured into a structured proof under #2. Re-checked: the exponential decay is uniform after
    enlarging the constant, since the transform is continuous and bounded on the compact complement
    of a large interval; Fourier inversion applies because both $f$ and its transform are integrable;
    Young's inequality scaled with $u$ proportional to abs xi and $v$ proportional to abs y gives
    $2 pi abs y abs xi <= (a_0/2) abs xi^p + C_1 abs y^q$; the integrand is then bounded by
    $C_0 e^{-a_0 abs xi^p/2}e^{C_1 abs y^q}$ with an integrable first factor, which gives local
    uniform convergence, differentiation under the integral sign and hence holomorphy; and the growth
    bound follows by integrating, using abs y <= abs z. Added: the uniformity step for the decay, the
    reason differentiation is legitimate, and the explicit constant
    $A_0=C_0\int e^{-a_0\abs\xi^p/2}\,d\xi$, all of which the earlier solution compressed. No
    defect found in the statement, Problem 1 of Chapter 4; no retained solution set covers it.
---

::: {.exercise}
Suppose $\hat{f}(\xi) = O(e^{-a\abs{\xi}^p})$ as $\abs{\xi} \to \infty$, for some $p > 1$. Then $f$ is holomorphic for all $z$ and satisfies the growth condition
$$
\abs{f(z)} \leq Ae^{C\abs{z}^q}
$$
for some $A, C > 0$, where $1/p + 1/q = 1$.

Note that on the one hand, when $p \to \infty$ then $q \to 1$, and this limiting case can be interpreted as part of Theorem 3.3. On the other hand, when $p \to 1$ then $q \to \infty$, and this limiting case in a sense brings us back to Theorem 2.1.

[Hint: To prove the result, use the inequality $-\xi^p + \xi u \leq u^q$, which is valid when $\xi$ and $u$ are non-negative. To establish this inequality, examine separately the cases $\xi^p \geq \xi u$ and $\xi^p < \xi u$; note also that the functions $\xi = u^{q-1}$ and $u = \xi^{p-1}$ are inverses of each other because $(p - 1)(q - 1) = 1$.]
:::

::: {.solution}
No retained solution set covers this problem, so the argument is the card's own; it is the printed hint, namely Young's inequality, applied to the Fourier inversion integral. Let $q$ satisfy $1/p+1/q=1$.

::: pf

::: {.pf-step #decay}
After enlarging the constant there are $C_0,a_0>0$ with $\abs{\widehat f(\xi)}\le C_0e^{-a_0\abs\xi^p}$ for all $\xi\in\RR$.

::: pf-proof
The hypothesis $\widehat f(\xi)=O(e^{-a\abs\xi^p})$ gives constants $C,a$ with $\abs{\widehat f(\xi)}\le Ce^{-a\abs\xi^p}$ for large $\abs\xi$, and $\widehat f$ is continuous and hence bounded on the remaining compact set; taking $a_0\le a$ small and $C_0$ larger than both the bound on the compact set and $C$ gives the display.
:::

:::

::: {.pf-step #inversion}
For real $z$, $f(z)=\int_{\RR}\widehat f(\xi)e^{2\pi i\xi z}\,d\xi$.

::: pf-proof
$\widehat f$ is integrable, its decay being exponential, and $f$ is integrable by hypothesis; Fourier inversion for functions in $L^1$ with integrable transform gives the displayed identity for real $z$.
:::

:::

::: {.pf-step #young}
For every $u,v\ge0$, $uv\le u^p/p+v^q/q$; consequently, with $z=x+iy$, there is $C_1=C_1(a_0,p)$ with
$$
2\pi\abs y\abs\xi\le\frac{a_0}{2}\abs\xi^p+C_1\abs y^q .
$$

::: pf-proof
Young's inequality is the concavity of the logarithm, or the convexity of $t\mapsto t^p$, applied to the two summands. Apply it to $u=(a_0p/4)^{1/p}\abs\xi$ and $v=(4/(a_0p))^{1/p}\pi\abs y$: the product $uv$ is a constant multiple of $\abs y\abs\xi$, the first summand is $(a_0/4)\abs\xi^p$ and the second is $C_1\abs y^q$ for a constant depending only on $a_0,p$; multiplying by the appropriate constant gives the displayed inequality with $a_0/2$ in place of $a_0/4$ after absorbing the constant factor.
:::

:::

::: {.pf-step #holomorphic}
The formula $F(z)=\int_{\RR}\widehat f(\xi)e^{2\pi i\xi z}\,d\xi$ defines an entire function, agreeing with $f$ on $\RR$.

::: pf-proof
For $z=x+iy$, steps [](#decay){.pf-ref} and [](#young){.pf-ref} give
$$
\abs{\widehat f(\xi)e^{2\pi i\xi z}}\le C_0e^{-a_0\abs\xi^p}e^{2\pi\abs y\abs\xi}\le C_0e^{-a_0\abs\xi^p/2}e^{C_1\abs y^q},
$$
and the first factor is integrable in $\xi$ since $p>1$. On a compact set of $z$ the second factor is uniformly bounded, so the integral converges locally uniformly; a locally uniformly convergent integral of holomorphic integrands may be differentiated under the integral sign to every order, so $F$ is holomorphic on $\CC$. By step [](#inversion){.pf-ref} it agrees with $f$ on the real axis, so it is the required entire extension.
:::

:::

::: {.pf-step}
$\boxed{\abs{f(z)}\le Ae^{C\abs z^q}}$ for constants $A,C>0$.

::: pf-proof
Integrating the bound of step [](#holomorphic){.pf-ref},
$$
\abs{f(z)}\le C_0\Bigl(\int_{\RR}e^{-a_0\abs\xi^p/2}\,d\xi\Bigr)e^{C_1\abs y^q}=A_0e^{C_1\abs y^q}
$$
with $A_0=C_0\int e^{-a_0\abs\xi^p/2}d\xi<\infty$; and $\abs y\le\abs z$, so taking $A=A_0$ and $C=C_1$ gives the stated growth condition with $1/p+1/q=1$.
:::

:::

:::
:::
