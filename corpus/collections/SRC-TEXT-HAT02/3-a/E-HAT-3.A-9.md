---
schema: qual/card@1
id: E-HAT-3.A-9
kind: problem
title: "Divisibility and torsion in Ext(A, Z) via the spliced Hom-Ext diagram"
classification:
  areas:
  - topology
  topics:
  - Cohomology
relations: []
review: draft
audit:
- event: source-checked
  by: claude
  date: 2026-11-02
  note: >-
    Statement transcribed from the printed page -- pages 320-321, rendered from tmp/hat/AT.pdf
    with pdftocairo at 400 dpi and read with the diagram cropped and magnified -- because the
    statement depends on the printed commutative diagram, which the text extraction does not
    carry. As rendered, the diagram's exact sequence across the top is the one displayed on the
    card, with Ext(pA,Z) between the two Ext(A,Z) terms, two diagonal arrows from the first
    Ext(A,Z) to Ext(pA,Z) and from Ext(pA,Z) to the second Ext(A,Z) composing to the horizontal
    multiplication-by-p, and the row 0 --> Hom(pA,Z) --iso--> Hom(A,Z) --> 0 below. New card:
    exercises 7, 8 and 9 of Section 3.A were uncarded; 9 completes the section.
- event: solution-written
  by: claude
  date: 2026-11-02
  note: >-
    Seven steps. The two six-term Hom-Ext sequences are recorded from the standard Hom-Ext long
    exact sequence; torsion groups have no maps into Z, which kills Hom(_pA,Z) and Hom(A_p,Z) and
    forces Hom(pA,Z) onto Hom(A,Z); the middle map is multiplication by p because the two maps on
    Ext are induced by j and q with j q = p; splicing gives the printed top row. The conclusions
    then read off it, with the one cited lemma that a p-torsion group with vanishing Hom and Ext
    into Z is zero, proved from Ext(Z/p,Z) = Z/p and Ext^2 = 0 over Z rather than assumed.
---

::: {.problem}
For an abelian group $A$ let $p:A\to A$ be multiplication by $p$, and let ${}_pA=\operatorname{Ker}p$, $pA=\operatorname{Im}p$, and $A_p=\operatorname{Coker}p$ as in the proof of Proposition 3F.12. Show that the six-term exact sequences involving $\operatorname{Hom}(-,\ZZ)$ and $\operatorname{Ext}(-,\ZZ)$ associated to the short exact sequences $0\to {}_pA\to A\to pA\to 0$ and $0\to pA\to A\to A_p\to 0$ can be spliced together to yield the exact sequence across the top of the following diagram:
$$
\operatorname{Hom}(pA,\ZZ)\longrightarrow\operatorname{Ext}(A_p,\ZZ)\longrightarrow\operatorname{Ext}(A,\ZZ)\xrightarrow{\ p\ }\operatorname{Ext}(A,\ZZ)\longrightarrow\operatorname{Ext}({}_pA,\ZZ)\longrightarrow 0,
$$
with $\operatorname{Ext}(pA,\ZZ)$ drawn between the two $\operatorname{Ext}(A,\ZZ)$ terms, arrows
$$
\operatorname{Ext}(A,\ZZ)\to\operatorname{Ext}(pA,\ZZ)\to 0
\qquad\text{and}\qquad
0\to\operatorname{Ext}(pA,\ZZ)\to\operatorname{Ext}(A,\ZZ)
$$
whose two middle maps compose to the horizontal map, and
$$
0\to\operatorname{Hom}(pA,\ZZ)\xrightarrow{\ \cong\ }\operatorname{Hom}(A,\ZZ)\longrightarrow 0
$$
below, where the map labeled $p$ is multiplication by $p$.

Use this to show:

(a) $\operatorname{Ext}(A,\ZZ)$ is divisible iff $A$ is torsionfree.

(b) $\operatorname{Ext}(A,\ZZ)$ is torsionfree if $A$ is divisible, and the converse holds if $\operatorname{Hom}(A,\ZZ)=0$.

:::

::: {.solution}

::: pf

::: {.pf-step #sequences}
Applying $\operatorname{Hom}(-,\ZZ)$ to the two short exact sequences gives six-term exact sequences
$$
0\to\operatorname{Hom}(pA,\ZZ)\to\operatorname{Hom}(A,\ZZ)\to\operatorname{Hom}({}_pA,\ZZ)\to\operatorname{Ext}(pA,\ZZ)\to\operatorname{Ext}(A,\ZZ)\to\operatorname{Ext}({}_pA,\ZZ)\to 0
$$
from $0\to {}_pA\xrightarrow{i}A\xrightarrow{q}pA\to 0$, and
$$
0\to\operatorname{Hom}(A_p,\ZZ)\to\operatorname{Hom}(A,\ZZ)\to\operatorname{Hom}(pA,\ZZ)\to\operatorname{Ext}(A_p,\ZZ)\to\operatorname{Ext}(A,\ZZ)\to\operatorname{Ext}(pA,\ZZ)\to 0
$$
from $0\to pA\xrightarrow{j}A\xrightarrow{k}A_p\to 0$.

::: pf-proof
These are the two instances of the standard long exact sequence of $\operatorname{Hom}$ and $\operatorname{Ext}$, which comes from applying $\operatorname{Hom}(-,\ZZ)$ to a short exact sequence $0\to X\to Y\to Z\to 0$: exactness of $0\to\operatorname{Hom}(Z,\ZZ)\to\operatorname{Hom}(Y,\ZZ)\to\operatorname{Hom}(X,\ZZ)$ is left exactness of $\operatorname{Hom}$, and $\operatorname{Ext}(H,\ZZ)=\operatorname{coker}\bigl(\operatorname{Hom}(H,\QQ)\to\operatorname{Hom}(H,\QQ/\ZZ)\bigr)$ from the injective resolution $0\to\ZZ\to\QQ\to\QQ/\ZZ\to0$ continues it as displayed, exact throughout.

:::

:::

::: {.pf-step #vanishing}
$\operatorname{Hom}({}_pA,\ZZ)=0$ and $\operatorname{Hom}(A_p,\ZZ)=0$.

::: pf-proof
Every element of ${}_pA$ is killed by $p$, and likewise every element of $A_p=A/pA$, since $p\bar a=\overline{pa}=0$. A homomorphism from a torsion group into the torsionfree group $\ZZ$ sends every element to an element killed by some nonzero integer, so it is zero.

:::

:::

::: {.pf-step #iso}
Precomposition with $q\colon A\to pA$ is an isomorphism $q^*\colon\operatorname{Hom}(pA,\ZZ)\cong\operatorname{Hom}(A,\ZZ)$.

::: pf-proof
The map $q$ is surjective, so $q^*$ is injective: if $f\circ q=0$ then $f=0$ since $q$ hits every element. For surjectivity, let $g\in\operatorname{Hom}(A,\ZZ)$; since ${}_pA$ is torsion, $g$ vanishes on ${}_pA=\ker q$ by step [](#vanishing){.pf-ref}, so $f(pa)=g(a)$ is well defined, is a homomorphism $pA\to\ZZ$, and satisfies $q^*f=g$.

:::

:::

::: {.pf-step #pmap}
The composite $\operatorname{Ext}(A,\ZZ)\to\operatorname{Ext}(pA,\ZZ)\to\operatorname{Ext}(A,\ZZ)$ of the two maps named in the problem is multiplication by $p$.

::: pf-proof
The two maps are induced by $j\colon pA\hookrightarrow A$ and $q\colon A\to pA$, and $jq\colon A\to A$ is multiplication by $p$. Functoriality of $\operatorname{Ext}(-,\ZZ)$ gives
$$
(jq)^*=q^*\circ j^*,
$$
and $(jq)^*$ on the Ext group is multiplication by $p$, because the maps of the defining Hom groups over $\QQ$ and $\QQ/\ZZ$ are multiplication by $p$ there.

:::

:::

::: {.pf-step #splice}
The printed top row
$$
\operatorname{Hom}(pA,\ZZ)\to\operatorname{Ext}(A_p,\ZZ)\to\operatorname{Ext}(A,\ZZ)\xrightarrow{\ p\ }\operatorname{Ext}(A,\ZZ)\to\operatorname{Ext}({}_pA,\ZZ)\to 0
$$
is exact.

::: pf-proof
Splice the two sequences of step [](#sequences){.pf-ref} at $\operatorname{Ext}(pA,\ZZ)$: the segment $0=\operatorname{Hom}({}_pA,\ZZ)\to\operatorname{Ext}(pA,\ZZ)\to\operatorname{Ext}(A,\ZZ)\to\operatorname{Ext}({}_pA,\ZZ)\to0$ with the vanishing of step [](#vanishing){.pf-ref}, and the segment $\operatorname{Hom}(pA,\ZZ)\to\operatorname{Ext}(A_p,\ZZ)\to\operatorname{Ext}(A,\ZZ)\to\operatorname{Ext}(pA,\ZZ)\to0$. Concatenating through the isomorphic $\operatorname{Ext}(pA,\ZZ)$ common to both gives an exact sequence, and steps [](#pmap){.pf-ref} names its middle map. Its exactness at $\operatorname{Hom}(pA,\ZZ)$ begins at the map induced by $k$, whose kernel is the image of $\operatorname{Hom}(A,\ZZ)\to\operatorname{Hom}(pA,\ZZ)$ from the second sequence.

:::

:::

::: {.pf-step #torsionout}
If $K$ is an abelian group with $pK=0$ and $\operatorname{Ext}(K,\ZZ)=0$, then $K=0$.

::: pf-proof
If $K\ne0$ choose $0\ne x\in K$; $pK=0$ makes $\langle x\rangle\cong\ZZ/p$. From $0\to\ZZ/p\to K\to K/\langle x\rangle\to0$, the connecting map out of $\operatorname{Ext}(\ZZ/p,\ZZ)$ is zero because $\operatorname{Ext}^2$ of abelian groups vanishes, so $\operatorname{Ext}(K,\ZZ)\to\operatorname{Ext}(\ZZ/p,\ZZ)$ is surjective. But $\operatorname{Ext}(\ZZ/p,\ZZ)\cong\ZZ/p$ by the six-term sequence of $0\to\ZZ\xrightarrow{p}\ZZ\to\ZZ/p\to0$, so $\operatorname{Ext}(K,\ZZ)\ne0$, a contradiction. (That $\operatorname{Ext}^2=0$ over $\ZZ$ is because every subgroup of a free abelian group is free, so every group has an injective resolution of length one.)

:::

:::

::: {.pf-step #conclusion}
Parts (a) and (b) follow from step [](#splice){.pf-ref}.

::: pf-proof
(a) If $A$ is torsionfree then ${}_pA=0$ and $\operatorname{Ext}({}_pA,\ZZ)=\operatorname{Ext}(0,\ZZ)=0$, so exactness at the second $\operatorname{Ext}(A,\ZZ)$ gives $\operatorname{im}(p)=\ker(\to\operatorname{Ext}({}_pA,\ZZ))=\operatorname{Ext}(A,\ZZ)$: multiplication by $p$ is surjective, for every $p$, so $\operatorname{Ext}(A,\ZZ)$ is divisible. Conversely if $\operatorname{Ext}(A,\ZZ)$ is divisible by every $p$, exactness makes the outgoing map to $\operatorname{Ext}({}_pA,\ZZ)$ zero, but that map is already surjective, so $\operatorname{Ext}({}_pA,\ZZ)=0$, and step [](#torsionout){.pf-ref} with $\operatorname{Hom}({}_pA,\ZZ)=0$ from [](#vanishing){.pf-ref} gives ${}_pA=0$ for every $p$, that is, $A$ torsionfree.

(b) If $A$ is divisible then $pA=A$, so $A_p=0$ and the top row has $0=\operatorname{Ext}(A_p,\ZZ)\to\operatorname{Ext}(A,\ZZ)$ as its first map: that map being zero makes the next map injective, so multiplication by $p$ is injective for every $p$ and $\operatorname{Ext}(A,\ZZ)$ is torsionfree. Conversely if $\operatorname{Ext}(A,\ZZ)$ is torsionfree, the $p$-map is injective, so by exactness the incoming map from $\operatorname{Ext}(A_p,\ZZ)$ is zero, so the map from $\operatorname{Hom}(pA,\ZZ)$ is surjective; but with $\operatorname{Hom}(A,\ZZ)=0$ its domain is $\operatorname{Hom}(pA,\ZZ)\cong\operatorname{Hom}(A,\ZZ)=0$ by step [](#iso){.pf-ref}, hence $\operatorname{Ext}(A_p,\ZZ)=0$, and $\operatorname{Hom}(A_p,\ZZ)=0$ from [](#vanishing){.pf-ref} with [](#torsionout){.pf-ref} gives $A_p=0$, that is, $pA=A$ for every $p$.

:::

:::

:::

:::
