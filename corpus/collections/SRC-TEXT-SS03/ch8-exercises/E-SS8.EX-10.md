---
schema: qual/card@1
id: E-SS8.EX-10
kind: problem
title: A Schwarz-type bound on the upper half-plane
classification:
  areas:
  - complex-analysis
  topics:
  - Schwarz Lemma
  - Automorphisms
relations: []
review: draft
audit:
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-11
- event: solution-written
  by: claude
  date: 2026-11-19
  note: >-
    Lamport structure over the prose that was already there. The biholomorphism of the
    half-plane with the disc is now verified from the modulus inequality |z-i| < |z+i| and
    by exhibiting the inverse, rather than quoted, and the hypotheses of Schwarz's lemma are
    checked one at a time on the transported function. Not checked: the book's own text of
    the exercise, since no copy of Stein and Shakarchi is retained in this checkout; the
    statement is as transcribed on the card. No retained solution set covers the exercise
    (the collection's provenance is a Google Books record), so the argument is the card's
    own. No statement repair.
---

::: {.exercise}
Let $F \colon \halfplane \to \CC$ be a holomorphic function that satisfies
$$
\abs{F(z)} \leq 1 \quad \text{and} \quad F(i) = 0.
$$
Prove that
$$
\abs{F(z)} \leq \abs{\frac{z - i}{z + i}} \quad \text{for all } z \in \halfplane.
$$
:::

::: {.solution}
No retained solution set covers this exercise: the collection's provenance is a Google Books record, so the argument is the card's own. Let $\halfplane=\{z:\operatorname{Im}z>0\}$, $\DD=\{w:\abs{w}<1\}$, and
$$
\phi(z)=\frac{z-i}{z+i},\qquad z\in\halfplane .
$$

::: pf

::: {.pf-step #biholo}
$\phi$ maps $\halfplane$ bijectively onto $\DD$, is holomorphic there, and $\phi(i)=0$.

::: pf-proof
For $z\in\halfplane$ the denominator does not vanish, since $z=-i$ has negative imaginary part, so $\phi$ is holomorphic on $\halfplane$. Compute $\abs{z-i}^2=\abs{z}^2-2\operatorname{Im}z+1$ and $\abs{z+i}^2=\abs{z}^2+2\operatorname{Im}z+1$, so $\abs{z-i}<\abs{z+i}$ exactly when $\operatorname{Im}z>0$; hence $\abs{\phi(z)}<1$ on $\halfplane$. Conversely, for $w\in\DD$ put $z=i\frac{1+w}{1-w}$, which is defined since $\abs{w}<1$ excludes $w=1$. Then $\operatorname{Im}z$ has the sign of $\operatorname{Re}\frac{1+w}{1-w}=\frac{1-\abs{w}^2}{\abs{1-w}^2}>0$, so $z\in\halfplane$, and solving $\phi(z)=w$ for $z$ gives exactly this $z$; so $\phi$ is onto. Finally $\phi(i)=\frac{i-i}{i+i}=0$.
:::

:::

::: {.pf-step #transport}
$g(w)=F\bigl(\phi^{-1}(w)\bigr)$ is holomorphic on $\DD$, satisfies $\abs{g(w)}\le1$ there, and $g(0)=0$.

::: pf-proof
$\phi^{-1}$ is holomorphic on $\DD$ because $\phi$ is a biholomorphism by step [](#biholo){.pf-ref} — equivalently the displayed formula for $z$ is holomorphic in $w$ on $\DD$ — so the composite of holomorphic functions is holomorphic. The bound is the hypothesis $\abs{F}\le1$ transported, and $g(0)=F(\phi^{-1}(0))=F(i)=0$ since $\phi(i)=0$.
:::

:::

::: {.pf-step #schwarz}
$\abs{g(w)}\le\abs{w}$ for all $w\in\DD$.

::: pf-proof
This is Schwarz's lemma applied to $g$: a holomorphic self-map of the disc fixing $0$ satisfies $\abs{g(w)}\le\abs{w}$ and $\abs{g'(0)}\le1$. Its proof writes $g(w)=w\,h(w)$ with $h$ holomorphic on $\DD$, and applies the maximum modulus principle to $h$ on discs of radius $r<1$ together with the bound $\abs{h}\le1/r$.
:::

:::

::: {.pf-step}
$\abs{F(z)}\le\abs{\dfrac{z-i}{z+i}}$ for all $z\in\halfplane$.

::: pf-proof
Let $z\in\halfplane$ and $w=\phi(z)\in\DD$. Then $F(z)=F(\phi^{-1}(w))=g(w)$, so $\abs{F(z)}=\abs{g(w)}\le\abs{w}=\abs{\phi(z)}$ by step [](#schwarz){.pf-ref}, and $\abs{\phi(z)}=\abs{(z-i)/(z+i)}$. This is the asserted inequality; equality at some interior point would force $g$ to be a rotation of the identity and hence $F$ a unimodular multiple of $\phi$, which the proof of Schwarz's lemma also gives.
:::

:::

:::

:::
