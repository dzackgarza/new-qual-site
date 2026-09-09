---
schema: qual/card@1
id: P-RAF05C
kind: problem
title: "e^x sin(e^x) defines a tempered distribution"
classification:
  areas:
  - real-analysis
  topics:
  - Tempered Distributions
  - Schwartz Space
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-30
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Checked against Problem 3 of the official UCSD Fall 2005 real-analysis qualifying exam.
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Corrected the sign in the distributional-derivative identity and normalized the solution/proof blocks.
---

::: problem
Show that the function $e^x \sin(e^x)$ defines a tempered distribution on $\mathbb{R}$.
(That is, show that the distribution it defines extends to a tempered distribution.)
:::

::: solution
<1>1. Let $f(x) = e^x \sin(e^x)$.
::: proof
definition.
:::

<1>2. $f$ is locally integrable, so it defines a distribution $T_f(\varphi) = \int_{\mathbb{R}} f(x)\varphi(x)\,dx$ on $C_c^\infty(\mathbb{R})$.
::: proof
$f$ is continuous, hence locally integrable.
:::

<1>3. $f$ is the derivative of a bounded function: $f(x) = -\frac{d}{dx}\cos(e^x)$.
::: proof
$\frac{d}{dx}\cos(e^x) = -e^x \sin(e^x) = -f(x)$.
:::

<1>4. Hence $T_f = -\frac{d}{dx} T_{\cos(e^x)}$, where $\cos(e^x)$ is a bounded (hence tempered) function.
::: proof
<1>3 and the definition of the distributional derivative.
:::

<1>5. A bounded function defines a tempered distribution, and the derivative of a tempered distribution is tempered.
::: proof
bounded functions are tempered (they grow at most polynomially), and the space of tempered distributions is closed under differentiation.
:::

<1>6. Hence $T_f$ is a tempered distribution.
::: proof
<1>4 and <1>5.
:::

<1>7. Q.E.D.
::: proof
<1>6.
:::
:::
