---
schema: qual/card@1
id: P-SAFVA
kind: problem
title: $\int\ln(ax+b)\,dx$ and logarithmic special cases
classification:
  areas:
  - prelim
  topics:
  - Integrals
  - Integration by Parts
relations: []
review: draft
audit:
- event: solution-written
  by: muse-spark-1.2
  date: 2026-08-30
---

::: {.problem}
1. $\displaystyle \int \ln (ax + b) ~dx = \color{blue} {\frac {ax + b}{a} \ln (ax + b) - x}$

- **Solution:** $u = \ln (ax + b)​$, $v = x​$, $du = \frac {a}{ax + b} ~dx​$, $dv = dx​$

  1. $\displaystyle \int \log _3 (x) ~dx = \color{blue} { \frac {x \ln (x) - x}{\ln (3)}}​$

  - **Solution:** $\log _3 (x) =  \frac {\ln (x)}{\ln (3)}$

  - **Used 2019**

  2. $\displaystyle \int_{1}^{e} \ln (\sqrt {x}) ~dx = \color{blue} { \frac {1}{2}}​$

  - **Solution:** $\ln (\sqrt {x}) =  \frac {1}{2} \ln (x)​$

  3. $\displaystyle \int \ln(x^2 + 6x + 5) ~dx = \color{blue} { (x + 1) \ln (x + 1) + (x + 5) \ln (x + 5) - 2x}​$

  - **Solution:** $\ln(x^2 + 6x + 5)=  \ln (x + 5)(x + 1) = \ln (x + 5) + \ln (x + 1)​$

  - **Used 2018**, *Unsolved*

  - **Used 2019**

  4. $\displaystyle \int \ln(x^2-1) ~dx =  \color{blue} { (x + 1) \ln(x + 1) + (x - 1) \ln(x - 1) - 2x}$
:::

::: {.solution}

::: pf

::: {.pf-step #s1}

Evaluation of the base integral $\int \ln(ax + b) \, dx$:

::: pf-proof

::: pf-step

Substitute $u = ax + b$, so $du = a \, dx \implies dx = \frac{1}{a} \, du$.
The integral becomes:
\[
\int \ln(ax + b) \, dx = \frac{1}{a} \int \ln(u) \, du.
\]

::: pf-proof

substitution method.

:::

:::

::: pf-step

Integrating by parts with $U = \ln u, \, dV = du \implies dU = \frac{1}{u} du, \, V = u$:
\[
\int \ln u \, du = u \ln u - \int 1 \, du = u \ln u - u + C.
\]

::: pf-proof

integration by parts.

:::

:::

::: pf-step

Substituting back $u = ax + b$:
\[
\int \ln(ax + b) \, dx = \frac{ax + b}{a} \ln(ax + b) - \frac{ax + b}{a} + C = \frac{ax + b}{a} \ln(ax + b) - x + C.
\]

::: pf-proof

absorbing the constant $-\frac{b}{a}$ into $C$.

:::

:::

:::

:::

::: {.pf-step #s2}

Evaluation of sub-problems (1) through (4):

::: pf-proof

::: pf-step

**Sub-problem 1: $\int \log_3(x) \, dx$**
Using the change of base formula $\log_3(x) = \frac{\ln x}{\ln 3}$:
\[
\int \log_3(x) \, dx = \frac{1}{\ln 3} \int \ln x \, dx = \frac{x \ln x - x}{\ln 3} + C.
\]

::: pf-proof

linearity of integration and step [](#s1){.pf-ref} (step [](#s2-2){.pf-ref}).

:::

:::

::: {.pf-step #s2-2}

**Sub-problem 2: $\int_1^e \ln(\sqrt{x}) \, dx$**
Using the logarithm power rule $\ln(\sqrt{x}) = \frac{1}{2} \ln x$:
\[
\int_1^e \ln(\sqrt{x}) \, dx = \frac{1}{2} \int_1^e \ln x \, dx = \frac{1}{2} \Big[ x \ln x - x \Big]_1^e = \frac{1}{2} \Big( (e - e) - (0 - 1) \Big) = \frac{1}{2}(1) = \frac{1}{2}.
\]

::: pf-proof

Fundamental Theorem of Calculus.

:::

:::

::: pf-step

**Sub-problem 3: $\int \ln(x^2 + 6x + 5) \, dx$**
Factoring $x^2 + 6x + 5 = (x + 1)(x + 5)$:
\[
\int \ln(x^2 + 6x + 5) \, dx = \int \ln(x + 1) \, dx + \int \ln(x + 5) \, dx.
\]
Applying step [](#s1){.pf-ref} to each term gives:
\[
\big((x + 1)\ln(x + 1) - x\big) + \big((x + 5)\ln(x + 5) - x\big) + C = (x + 1)\ln(x + 1) + (x + 5)\ln(x + 5) - 2x + C.
\]

::: pf-proof

logarithm product rule and step [](#s1){.pf-ref}.

:::

:::

::: pf-step

**Sub-problem 4: $\int \ln(x^2 - 1) \, dx$**
Factoring $x^2 - 1 = (x - 1)(x + 1)$:
\[
\int \ln(x^2 - 1) \, dx = \int \ln(x - 1) \, dx + \int \ln(x + 1) \, dx = (x - 1)\ln(x - 1) + (x + 1)\ln(x + 1) - 2x + C.
\]

::: pf-proof

logarithm product rule and step [](#s1){.pf-ref}.

:::

:::

:::

:::

::: pf-qed

Step [](#s1){.pf-ref} evaluates $\int\ln(ax+b)\,dx$, and step [](#s2){.pf-ref} evaluates the four special cases.

:::

:::

:::
