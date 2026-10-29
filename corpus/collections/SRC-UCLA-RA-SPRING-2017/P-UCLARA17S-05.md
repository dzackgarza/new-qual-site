---
schema: qual/card@1
id: P-UCLARA17S-05
kind: problem
title: Decay of Fourier coefficients passes to absolutely continuous measures
classification:
  areas:
  - real-analysis
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-13
  note: Transcribed from the official UCLA Analysis Qualifying Exam, Spring 2017, and reconciled with the retained UCLA Analysis Qualifying Exam Solutions compendium.
- event: source-checked
  by: claude-opus-5-5
  date: 2026-10-29
  note: The source places the measures on the closed interval [0,1], where mu = delta_0 - delta_1 and nu = delta_0 refute the claim. The statement now places them on [0,1).
---

::: {.problem}
Let $d\mu$ be a finite complex Borel measure on $[0,1)$ such that
$$
\widehat\mu(n)=\int_0^1 e^{2\pi i n x}\,d\mu(x)\to0\qquad(n\to\infty).
$$
Let $d\nu$ be a finite complex Borel measure on $[0,1)$ absolutely continuous with respect to $d\mu$. Show that
$$
\widehat\nu(n)\to0\qquad(n\to\infty).
$$
:::

::: {.solution}
Identify $[0,1)$ with the circle $\circlegroup=\RR/\ZZ$ by $x\mapsto x+\ZZ$; this is a Borel isomorphism under which $e^{2\pi i n x}$ is a continuous character of $\circlegroup$.

::: pf

::: {.pf-step #s1}
Write $d\nu=f\,d\mu$ with $f\in L^1(|\mu|)$, and fix $\varepsilon>0$. There is a trigonometric polynomial
$$
P(x)=\sum_{m=-N}^N c_m e^{2\pi i m x}
$$
with $\int_{\circlegroup}|f-P|\,d|\mu|<\varepsilon$.

::: pf-proof
The density $f$ exists by the Radon--Nikodym theorem for complex measures.
Continuous functions are dense in $L^1(|\mu|)$ on the compact metric space $\circlegroup$, and trigonometric polynomials are uniformly dense in $C(\circlegroup)$ by the Stone--Weierstrass theorem; since $|\mu|$ is finite, uniform approximation controls the $L^1(|\mu|)$ distance.
:::

:::

::: {.pf-step #s2}
$\limsup_{n\to\infty}|\widehat\nu(n)|\le\varepsilon$.

::: pf-proof
For every $n$,
$$
\left|\widehat\nu(n)-\int_{\circlegroup}e^{2\pi i n x}P(x)\,d\mu(x)\right|
=\left|\int_{\circlegroup}e^{2\pi i n x}(f-P)\,d\mu\right|
\le\int_{\circlegroup}|f-P|\,d|\mu|
<\varepsilon,
$$
and
$$
\int_{\circlegroup}e^{2\pi i n x}P(x)\,d\mu(x)
=\sum_{m=-N}^N c_m\widehat\mu(n+m)
\longrightarrow0
$$
because the sum is finite and $n+m\to\infty$.
:::

:::

::: pf-qed
Since $\varepsilon>0$ is arbitrary, step [](#s2){.pf-ref} gives $\boxed{\widehat\nu(n)\to0}$.
:::

:::
:::
