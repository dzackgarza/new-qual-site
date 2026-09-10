---
schema: qual/card@1
id: P-ARTALG-AL04-10
kind: problem
title: 'Non-Galois cubics and cubic subfields of a degree-$105$ Galois extension'
classification:
  areas:
  - algebra
  topics:
  - Galois Theory
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-29
- event: source-checked
  by: chatgpt
  date: 2026-09-10
  note: "Visually checked PDF page 37, Fields 3. The scan prints [K:F]=105 with F undefined; the existing card's explicit degree hypothesis [K:Q]=105 is retained. Both requested conclusions were compared with the source."
- event: solution-written
  by: chatgpt
  date: 2026-09-10
  note: "Replaced the unsupported inference from an abelian normal subgroup and cyclic quotient with a direct coset-action proof."
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-10
  note: "Checked irreducibility and failure of normality for the real cubic, both image-order divisibilities in S3, equality of the action kernel with the index-three subgroup, and the final Galois correspondence."
---

::: problem
(a) Give an example of an extension of degree 3 over $\mathbb{Q}$ which is not Galois over $\mathbb{Q}$.

(b) Suppose $K$ is a Galois extension of $\mathbb{Q}$ with $[K:\mathbb{Q}] = 105$, and that $L$ is a subfield of $K$ with $[L:\mathbb{Q}] = 3$.
Show that $L$ is Galois over $\mathbb{Q}$.
:::

::: solution
<1>1. For part (a), $\mathbb Q(\sqrt[3]{2})$ is a non-Galois
extension of degree $3$.

::: proof
Let $a=\sqrt[3]{2}>0$. Eisenstein's criterion at $2$ makes
$x^3-2$ irreducible over $\mathbb Q$, so
$[\mathbb Q(a):\mathbb Q]=3$ [@DF04]. The other two roots
are $a\omega$ and $a\omega^2$ for a primitive cube root of
unity $\omega$. They are nonreal, whereas $\mathbb Q(a)$ is
contained in $\mathbb R$. Thus an irreducible polynomial over
the base field has a root in the extension but does not split
there. The extension is not normal and hence not Galois.
:::

<1>2. For part (b), $H=\operatorname{Gal}(K/L)$ is a normal
subgroup of $G=\operatorname{Gal}(K/\mathbb Q)$.

::: proof
The finite Galois correspondence gives $|G|=105$ and
$[G:H]=[L:\mathbb Q]=3$, hence $|H|=35$ [@DF04].
Let $G$ act by left multiplication on the three left cosets
of $H$, giving $\rho:G\to S_3$.
The action is transitive: $yx^{-1}$ sends $xH$ to $yH$.

The order of the image divides $105$, by the first isomorphism
theorem, and divides $6=|S_3|$, by Lagrange's theorem.
It is therefore $1$ or $3$. Transitivity on three points
excludes order $1$, so $|\rho(G)|=3$ and $|\ker\rho|=35$.
Every element of the kernel fixes the coset $H$, so belongs to
$H$. Since both subgroups have order $35$, $H=\ker\rho$.
Kernels are normal, proving the claim without any assumption
that a subgroup of index three is always normal.
:::

<1>3. The field $L$ in part (b) is Galois over $\mathbb Q$.

::: proof
An intermediate field of a finite Galois extension is Galois
over the base exactly when its corresponding subgroup is normal
[@DF04]. Apply this criterion to the subgroup in step <1>2.
:::
:::
