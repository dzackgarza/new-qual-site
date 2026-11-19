---
schema: qual/card@1
id: P-3MDGM
kind: problem
title: Antiderivatives of $(\sec^3 x+e^{\sin x})/\sec x$ and $1/(\tan x+\cot x)$
classification:
  areas:
  - prelim
  topics:
  - Integrals
  - Trigonometry
  - u-Substitution
relations: []
review: draft
audit:
- event: source-checked
  by: claude
  date: 2026-11-19
  note: >-
    Provenance repaired, the defect this date's COMPLAINTS screen recorded (the solution opened with
    the step statement, leaving no place for a provenance sentence). The solution now opens with one:
    the argument is the card's own, from $\sec x\cos x=1$, from $\tan x+\cot x=1/(\sin x\cos x)$
    and from the substitution $u=\sin x$. The collection has no retained source --- its
    `provenance:` is empty and its `source_kind` is `homework` --- so no page is cited. Both
    antiderivatives were recomputed here and stand: $\tan x+e^{\sin x}+C$ and
    $\tfrac12\sin^2x+C=-\tfrac12\cos^2x+C'$. Checked: `qualc.authoring check`; the Lamport filter,
    steps 1, 1.1--1.4, 2, 2.1--2.4 with QED present. Not checked: no source exists to check the sheet
    against, the two statements being read off the card's own problem block.
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-25
- event: solution-written
  by: claude
  date: 2026-11-19
  note: >-
    Every step now carries a pf-proof: the two containers state why their subclaims suffice, and the 8 leaf
    steps that asserted their claim with no justification each carry a sentence deriving it. Both
    antiderivatives were checked by differentiating: $\tan x+e^{\sin x}$ and $\sin^2x/2$. The card's
    provenance paragraph is unchanged and no source is claimed for it. Nothing in the statement was
    changed.

---

::: {.problem}
Evaluate, on intervals where the integrands are defined,

(a) $\displaystyle\int\frac{\sec^3x+e^{\sin x}}{\sec x}\,dx$;

(b) $\displaystyle\int\frac{dx}{\tan x+\cot x}$.
:::

::: {.solution}

The argument is the card's own: both antiderivatives follow from $\sec x\cos x=1$, from $\tan x+\cot x=1/(\sin x\cos x)$ and from the substitution $u=\sin x$, with no source transcribed. The collection records no retained problem or answer sheet --- its `provenance:` list is empty and its `source_kind` is `homework` --- so no printed page is cited here, and none is implied.

::: pf

::: pf-step
$\int \frac{\sec^3(x) + e^{\sin(x)}}{\sec(x)} \, dx = \tan(x) + e^{\sin(x)} + C$.

::: pf-proof

::: pf-step
Simplify the integrand algebraically using $\frac{1}{\sec(x)} = \cos(x)$: $$\frac{\sec^3(x) + e^{\sin(x)}}{\sec(x)} = \sec^2(x) + \cos(x) e^{\sin(x)}.$$

::: pf-proof
Dividing by $\sec x$ multiplies by $\cos x$, which gives the two terms displayed.
:::

:::

::: pf-step
Integrate term-by-term: $$\int \sec^2(x) \, dx = \tan(x) + C_1.$$

::: pf-proof
The derivative of $\tan x$ is $\sec^2x$.
:::

:::

::: pf-step
For $\int \cos(x) e^{\sin(x)} \, dx$, substitute $u = \sin(x) \implies du = \cos(x) \, dx$: $$\int \cos(x) e^{\sin(x)} \, dx = \int e^u \, du = e^u + C_2 = e^{\sin(x)} + C_2.$$

::: pf-proof
The substitution has $du=\cos x\,dx$, so the integral becomes $\int e^u\,du=e^u+C_2$.
:::

:::

::: pf-step
Combining yields $\tan(x) + e^{\sin(x)} + C$.

::: pf-proof
Adding the two antiderivatives and absorbing the two constants into one.
:::

:::

:::

:::

::: pf-step
$\int \frac{1}{\tan(x) + \cot(x)} \, dx = \frac{1}{2}\sin^2(x) + C = -\frac{1}{2}\cos^2(x) + C'$.

::: pf-proof

::: pf-step
Rewrite trigonometric functions in terms of $\sin(x)$ and $\cos(x)$: $$\tan(x) + \cot(x) = \frac{\sin(x)}{\cos(x)} + \frac{\cos(x)}{\sin(x)} = \frac{\sin^2(x) + \cos^2(x)}{\sin(x)\cos(x)} = \frac{1}{\sin(x)\cos(x)}.$$

::: pf-proof
Writing each function as a quotient over the common denominator and using $\sin^2x+\cos^2x=1$.
:::

:::

::: pf-step
Thus the integrand is $\frac{1}{\tan(x) + \cot(x)} = \sin(x)\cos(x)$.

::: pf-proof
Taking the reciprocal of the identity just obtained.
:::

:::

::: pf-step
Using the substitution $u = \sin(x) \implies du = \cos(x) \, dx$: $$\int \sin(x)\cos(x) \, dx = \int u \, du = \frac{1}{2} u^2 + C = \frac{1}{2}\sin^2(x) + C.$$

::: pf-proof
With $du=\cos x\,dx$ the integral becomes $\int u\,du=u^2/2+C$.
:::

:::

::: pf-step
Using $\sin^2(x) = 1 - \cos^2(x)$, this equals $-\frac{1}{2}\cos^2(x) + C'$.

::: pf-proof
Substituting the Pythagorean identity and absorbing the constant $1/2$.
:::

:::

:::

:::

:::
:::
