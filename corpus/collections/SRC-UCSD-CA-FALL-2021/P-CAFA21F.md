---
schema: qual/card@1
id: P-CAFA21F
kind: problem
title: "Entire function with modulus 1 on the unit circle"
classification:
  areas:
  - complex-analysis
  topics:
  - Complex Analysis
relations: []
review: draft
audit:
- event: source-checked
  by: claude
  date: 2026-11-19
  note: >-
    Read against the exam paper retained at assets/attachments/FA21-Complex.pdf, Problem 6 (10
    points): "Let f : C -> C be an entire function such that |f(z)| = 1 for |z| = 1. Show that there
    exists a in C and n >= 0 such that f(z) = a z^n." The card's statement is that problem verbatim.
- event: solution-reviewed
  by: claude
  date: 2026-11-19
  note: >-
    The proof was wrong in its first claim and was replaced in this pass. It said the zeros of f in
    the disc are finite because f has no zeros on the unit circle, which does not follow: an entire
    function can have zeros accumulating on the circle, and a Blaschke product over them would not
    be finite, so the subsequent cancellation argument covered only the case the hypothesis does not
    give. The proof now uses the reflection identity: f*(z) = 1/conj(f(1/conj z)) is meromorphic on
    C minus 0 and agrees with f on the unit circle, so f(z) conj(f(1/conj z)) = 1 identically, which
    excludes every zero off the origin; then f = z^n h with h entire and nonvanishing, and |h| = 1 on
    the circle forces h constant by the maximum modulus principle applied to h and 1/h. The
    conclusion f(z) = a z^n with |a| = 1 is unchanged.
---

::: {.problem}
Let $f : \CC \to \CC$ be an entire function such that $\abs{f(z)} = 1$ for $\abs{z} = 1$.
Show that there exists $a \in \CC$ and $n \geq 0$ such that $f(z) = az^n$.
:::

::: {.solution}
This is Problem 6 (10 points) of the UCSD complex-analysis qualifying exam of Fall 2021 (`assets/attachments/FA21-Complex.pdf`). No published solution set is transcribed: the argument is the card's own.

What was repaired: the card assumed that $f$ has only finitely many zeros in $\DD$ because $f$ has none on $\abs{z}=1$, which does not follow — zeros of an entire function may accumulate on the circle — and it then argued with a Blaschke product that would have to have finitely many factors. The substitution below avoids the count entirely: the reflection identity $f(z)\overline{f(1/\overline{z})}=1$ shows at once that $f$ has no zeros off the origin.

::: pf

::: {.pf-step #reflection}
For $z\neq0$ the function $f^{*}(z)=1/\overline{f(1/\overline{z})}$ is meromorphic, and $f^{*}=f$ on $\abs{z}=1$; hence $f(z)\overline{f(1/\overline{z})}=1$ for every $z\neq0$.

::: pf-proof
The map $z\mapsto\overline{f(1/\overline{z})}$ is holomorphic on $\CC\setminus\{0\}$: it is the composite of the holomorphic $f$, the antiholomorphic $z\mapsto1/\overline{z}$ and complex conjugation, and the two conjugations cancel. It is not identically zero, since $f$ is not, so its reciprocal $f^{*}$ is meromorphic on $\CC\setminus\{0\}$. For $\abs{z}=1$ one has $1/\overline{z}=z$, so $f^{*}(z)=1/\overline{f(z)}=f(z)$, the last equality because $\abs{f(z)}=1$. The difference $f-f^{*}$ is meromorphic on the domain $\CC\setminus\{0\}$ and vanishes on the circle, which has accumulation points there, so the identity theorem for meromorphic functions gives $f=f^{*}$, that is $f(z)\overline{f(1/\overline{z})}=1$.
:::
:::

::: {.pf-step #nozeros}
$f$ has no zeros at all: $f(a)=0$ implies $a=0$.

::: pf-proof
Suppose $f(a)=0$ with $a\neq0$. If $\abs{a}=1$ this contradicts $\abs{f(a)}=1$. Otherwise apply the identity of step [](#reflection){.pf-ref} at $z=a$: it gives $0\cdot\overline{f(1/\overline{a})}=1$, which is impossible since $f$ is entire and $1/\overline{a}$ is a point where $f$ is finite. So the only possible zero of $f$ is $0$.
:::
:::

::: {.pf-step #monomial}
There are $n\geq0$ and an entire zero-free $h$ with $f(z)=z^{n}h(z)$.

::: pf-proof
By step [](#nozeros){.pf-ref} the function $f$ vanishes at $0$ to some finite order $n$ or not at all, and $h(z)=f(z)/z^{n}$ is entire and nowhere zero. If $f(0)\neq0$ take $n=0$.
:::
:::

::: {.pf-step #constant}
$h$ is constant, so $f(z)=az^{n}$ with $\abs{a}=1$.

::: pf-proof
$h$ is entire and nonvanishing, so $1/h$ is entire. On $\abs{z}=1$ one has $\abs{h(z)}=\abs{f(z)}=1$. The maximum modulus principle applied to $h$ in $\DD$ gives $\abs{h}\leq1$ there, and applied to $1/h$ gives $\abs{1/h}\leq1$, that is $\abs{h}\geq1$; so $\abs{h}=1$ on $\DD$, and a holomorphic function of constant modulus on a domain is constant. Hence $h\equiv a$ with $\abs{a}=1$.
:::
:::
:::

:::
