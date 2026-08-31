---
schema: qual/card@1
id: P-AMD-5VPC4U77
kind: problem
title: 'Given: $G = H \semidirect_\psi K$'
classification:
  areas:
  - algebra
  topics:
  - Semidirect Products
  - Automorphisms
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-29
---

::: {.problem}
Given: $G = H \semidirect_\psi K$ $$\psi: K \rightarrow Aut(H) \\ k \mapsto \psi(k)$$ $\theta \in Aut(H)$ $\rho: K \rightarrow K$ $$\phi_\theta: Aut(H) \rightarrow Aut(H) \\ \rho \mapsto \theta \circ \rho \circ \theta^{-1}$$ $$\psi_2: K \rightarrow Aut(H) \\ k \mapsto (\phi_\theta \circ \psi)(k)$$ $$\psi_3: K \rightarrow Aut(H) \\ k \mapsto (\psi \circ \rho)(k)$$

Show: $H \semidirect_\psi K \cong H \semidirect_{\psi_2} K \cong H \semidirect_{\psi_3} K$
:::

::: {.solution}
<1>1. $H \rtimes_\psi K \cong H \rtimes_{\psi_2} K$.
<2>1. Define $\Phi: H \rtimes_\psi K \to H \rtimes_{\psi_2} K$ by $\Phi(h, k) = (\theta(h), k)$.
::: {.proof}
definition.
:::
<2>2. $\Phi$ is a homomorphism.
::: {.proof}
in $H \rtimes_\psi K$, $(h_1, k_1)(h_2, k_2) = (h_1 \psi(k_1)(h_2), k_1 k_2)$; applying $\Phi$ gives $(\theta(h_1 \psi(k_1)(h_2)), k_1 k_2) = (\theta(h_1) \theta(\psi(k_1)(h_2)), k_1 k_2) = (\theta(h_1) (\theta \circ \psi(k_1) \circ \theta^{-1})(\theta(h_2)), k_1 k_2) = (\theta(h_1) \psi_2(k_1)(\theta(h_2)), k_1 k_2)$, which is exactly the product $(\theta(h_1), k_1)(\theta(h_2), k_2)$ in $H \rtimes_{\psi_2} K$.
:::
<2>3. $\Phi$ is bijective.
::: {.proof}
$\theta$ is an automorphism of $H$, so $\Phi$ has inverse $(h, k) \mapsto (\theta^{-1}(h), k)$.
:::
<2>4. Hence $H \rtimes_\psi K \cong H \rtimes_{\psi_2} K$.
::: {.proof}
<2>2 and <2>3.
:::

<1>2. $H \rtimes_\psi K \cong H \rtimes_{\psi_3} K$.
<2>1. Define $\Psi: H \rtimes_{\psi_3} K \to H \rtimes_\psi K$ by $\Psi(h, k) = (h, \rho(k))$.
::: {.proof}
definition (note the direction: $\psi_3 = \psi \circ \rho$).
:::
<2>2. $\Psi$ is a homomorphism.
::: {.proof}
in $H \rtimes_{\psi_3} K$, $(h_1, k_1)(h_2, k_2) = (h_1 \psi_3(k_1)(h_2), k_1 k_2) = (h_1 \psi(\rho(k_1))(h_2), k_1 k_2)$; applying $\Psi$ gives $(h_1 \psi(\rho(k_1))(h_2), \rho(k_1 k_2)) = (h_1 \psi(\rho(k_1))(h_2), \rho(k_1)\rho(k_2))$, which equals the product $(h_1, \rho(k_1))(h_2, \rho(k_2))$ in $H \rtimes_\psi K$.
:::
<2>3. $\Psi$ is bijective.
::: {.proof}
$\rho$ is an automorphism of $K$, so $\Psi$ has inverse $(h, k) \mapsto (h, \rho^{-1}(k))$.
:::
<2>4. Hence $H \rtimes_{\psi_3} K \cong H \rtimes_\psi K$, so $H \rtimes_\psi K \cong H \rtimes_{\psi_3} K$.
::: {.proof}
<2>2 and <2>3.
:::

<1>3. Q.E.D.
::: {.proof}
<1>1 and <1>2.
:::
:::
