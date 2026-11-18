---
schema: qual/card@1
id: P-CAFA25C
kind: problem
title: "Biholomorphic map between simply connected regions: existence, derivative bound, and equality"
classification:
  areas:
  - complex-analysis
  topics:
  - Conformal Maps
  - Riemann Mapping Theorem
  - Schwarz Lemma
  - Biholomorphic Maps
relations: []
review: draft
audit:
  - event: solution-reviewed
    by: claude
    date: 2026-11-18
    note: >-
      Restructured into Lamport steps, and the audit list this card lacked is created here. The
      source is a course examination, so there is no retained solution set behind the card and the
      problem statement is the source. Each part re-read: the Riemann maps are normalised by a disc
      automorphism; f = phi_2^{-1} o phi_1 is the biholomorphism asked for in (i); composing an
      arbitrary g with the two maps gives a self-map of the disc fixing 0, so Schwarz bounds its
      derivative by 1; the chain rule converts that into the derivative bound of (ii), and the same
      chain rule evaluates f'; and equality is exactly the equality case of Schwarz, which makes g
      biholomorphic. Part (iii) is now proved in both directions rather than only located. Not
      claimed: any statement for regions that are not simply connected, where no Riemann map exists.
---

::: {.problem}
Suppose $R_1, R_2$ are bounded simply connected regions in $\CC$.
Let $z_1 \in R_1$ and $z_2 \in R_2$.

(i) Prove that there exists a holomorphic bijective function $f : R_1 \to R_2$ such that $f(z_1) = z_2$.

(ii) Suppose that $g : R_1 \to R_2$ is a holomorphic function such that $g(z_1) = z_2$.
Prove that $\abs{g'(z_1)} \leq \abs{f'(z_1)}$.

(iii) When does equality occur in (ii)?
:::

::: {.solution}
The argument is the card's own; the collection is a course examination, so there is no printed solution set behind the card and the problem statement is the source.

::: pf

::: {.pf-step #riemann}
There are biholomorphisms $\phi_{j}:R_{j}\to\DD$ with $\phi_{j}(z_{j})=0$, $j=1,2$.

::: pf-proof
The Riemann mapping theorem gives a biholomorphism of each bounded simply connected region $R_{j}$ onto $\DD$; composing it with the automorphism $w\mapsto\frac{w-\phi(z_{j})}{1-\overline{\phi(z_{j})}w}$ of the disc, which is a biholomorphism sending $\phi(z_{j})$ to $0$, gives the required $\phi_{j}$.
:::

:::

::: {.pf-step #existence}
$f=\phi_{2}^{-1}\circ\phi_{1}$ is a biholomorphism $R_{1}\to R_{2}$ with $f(z_{1})=z_{2}$.

::: pf-proof
$\phi_{1}$ and $\phi_{2}^{-1}$ are biholomorphisms, so their composite is one; and $f(z_{1})=\phi_{2}^{-1}(0)=z_{2}$ because $\phi_{2}(z_{2})=0$. This is part (i).
:::

:::

::: {.pf-step #schwarz}
For holomorphic $g:R_{1}\to R_{2}$ with $g(z_{1})=z_{2}$, the map $G=\phi_{2}\circ g\circ\phi_{1}^{-1}:\DD\to\DD$ satisfies $G(0)=0$ and $\abs{G'(0)}\le1$.

::: pf-proof
$G$ is holomorphic as a composite of holomorphic maps, and $G(0)=\phi_{2}(g(z_{1}))=\phi_{2}(z_{2})=0$; Schwarz's lemma applies and gives $\abs{G'(0)}\le1$.
:::

:::

::: {.pf-step #chain}
$\abs{G'(0)}=\dfrac{\abs{\phi_{2}'(z_{2})}\,\abs{g'(z_{1})}}{\abs{\phi_{1}'(z_{1})}}$.

::: pf-proof
The chain rule gives $G'(0)=\phi_{2}'(z_{2})\,g'(z_{1})\,(\phi_{1}^{-1})'(0)$, and $(\phi_{1}^{-1})'(0)=1/\phi_{1}'(z_{1})$ by the inverse function theorem. Taking absolute values gives the displayed identity; all the derivatives are nonzero because each $\phi_{j}$ is a biholomorphism.
:::

:::

::: {.pf-step #bound}
$\abs{g'(z_{1})}\le\abs{f'(z_{1})}$.

::: pf-proof
Steps [](#schwarz){.pf-ref} and [](#chain){.pf-ref} give $\abs{g'(z_{1})}\le\abs{\phi_{1}'(z_{1})}/\abs{\phi_{2}'(z_{2})}$. On the other hand $f=\phi_{2}^{-1}\circ\phi_{1}$ gives, by the chain rule and $(\phi_{2}^{-1})'(0)=1/\phi_{2}'(z_{2})$, that $\abs{f'(z_{1})}=\abs{\phi_{1}'(z_{1})}/\abs{\phi_{2}'(z_{2})}$. Hence
$$
\boxed{\abs{g'(z_{1})}\le\abs{f'(z_{1})}.}
$$
This is part (ii).
:::

:::

::: {.pf-step #equality}
Equality holds exactly when $g$ is a biholomorphism $R_{1}\to R_{2}$ carrying $z_{1}$ to $z_{2}$.

::: pf-proof
By steps [](#chain){.pf-ref} and [](#bound){.pf-ref}, equality is equivalent to $\abs{G'(0)}=1$ with $G(0)=0$, which by the equality case of Schwarz's lemma is equivalent to $G(z)=e^{i\theta}z$ for some $\theta\in\RR$. That is $g=\phi_{2}^{-1}\circ(e^{i\theta}\mathrm{id})\circ\phi_{1}$, a composite of biholomorphisms, hence a biholomorphism; conversely a biholomorphic $g$ has $\abs{G'(0)}=1$ because $G$ is then an automorphism of the disc fixing $0$.
:::

:::

::: {.pf-step}
Parts (i), (ii) and (iii) hold.

::: pf-proof
Steps [](#existence){.pf-ref}, [](#bound){.pf-ref} and [](#equality){#equality} are the three parts:
$$
\boxed{\exists f\text{ biholomorphic};\quad \abs{g'(z_{1})}\le\abs{f'(z_{1})};\quad \text{equality iff }g\text{ is biholomorphic}.}
$$
:::

:::

:::
:::
