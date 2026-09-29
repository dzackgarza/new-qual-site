---
schema: qual/card@1
id: P-TOPS24C
kind: problem
title: Long exact sequence of a mapping cone
classification:
  areas:
  - topology
  topics:
  - Homology
  - Cell Complexes
relations: []
review: draft
---

::: {.problem}
The cone $CX$ of a space $X$ is $X \times I$ with $X \times \{0\}$ crushed to a point.
The mapping cone of a map $f \colon X \to Y$ is the space $C_f$ obtained by gluing $CX$ to $Y$ using the map $f \colon X \times \{1\} \to Y$.
Show that there is a long exact sequence
\[
\cdots \to H_i X \to H_i Y \to \widetilde{H}_i C_f \to H_{i-1} X \to \cdots.
\]
:::

::: {.solution}

::: pf

::: {.pf-step #cofiber-is-suspension}
The inclusion $Y\hookrightarrow C_f$ is a cofibration and the quotient is
$$C_f/Y\cong\Sigma X.$$

::: pf-proof
After collapsing $Y$ to a point, the copy of $CX$ has both its cone vertex and its base $X\times\{1\}$ collapsed to points, which is precisely the suspension of $X$.
:::

:::

::: {.pf-step #relative-homology-identification}
Hence
$$H_i(C_f,Y)\cong\widetilde H_i(C_f/Y)\cong\widetilde H_i(\Sigma X)\cong\widetilde H_{i-1}(X).$$

::: pf-proof
The first isomorphism is the standard identification of relative homology with reduced homology of the quotient for a good pair; the second uses step [](#cofiber-is-suspension){.pf-ref}, and the third is the suspension isomorphism.
:::

:::

::: pf-step
The long exact sequence of the pair $(C_f,Y)$ becomes
$$\cdots\to H_i(Y)\to \widetilde H_i(C_f)\to H_{i-1}(X)\to H_{i-1}(Y)\to\cdots.$$

::: pf-proof
Insert the identification from step [](#relative-homology-identification){.pf-ref} into the pair sequence. In positive degrees ordinary and reduced homology agree, while the reduced formulation handles degree zero uniformly.
:::

:::

::: pf-step
Under these identifications, the connecting map $H_i(X)\to H_i(Y)$ is $f_*$. Thus one obtains the cofiber exact sequence
$$\boxed{\cdots\to H_i(X)\xrightarrow{f_*}H_i(Y)\to\widetilde H_i(C_f)\to H_{i-1}(X)\xrightarrow{f_*}\cdots.}$$

::: pf-proof
Naturality of the boundary map for the cone pair identifies it with the map induced by the attaching map $f:X\to Y$. This is the standard homology exact sequence of the cofibration $X\xrightarrow fY\to C_f$.
:::

:::

:::

:::
