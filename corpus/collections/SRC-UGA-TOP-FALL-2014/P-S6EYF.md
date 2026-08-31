---
schema: qual/card@1
id: P-S6EYF
kind: problem
title: Integral homology of the union of the unit sphere and the ellipsoid $x^2+y^2+z^2/4=1$
classification:
  areas:
  - topology
  topics:
  - Homology
  - Mayer-Vietoris
relations: []
review: draft
---

::: problem
Compute the integral homology groups $H_k(X; \mathbb{Z})$ of the space $X = Y \cup Z \subset \mathbb{R}^3$, where $Y$ is the sphere
$$
Y = \{ (x, y, z) \in \mathbb{R}^3 \mid x^2 + y^2 + z^2 = 1 \}
$$
and $Z$ is the ellipsoid
$$
Z = \left\{ (x, y, z) \in \mathbb{R}^3 \;\middle|\; x^2 + y^2 + \frac{z^2}{4} = 1 \right\}.
$$
:::

::: solution
**Goal:** Compute the integral homology groups $H_k(X; \mathbb{Z})$ for all $k \ge 0$ using the Mayer–Vietoris sequence.

<1>1. Topology of the pieces and their intersection:
    *Proof:*
    <2>1. $Y = \{x^2 + y^2 + z^2 = 1\} \cong S^2$ is the standard unit 2-sphere.
    <2>2. $Z = \{x^2 + y^2 + z^2/4 = 1\} \cong S^2$ is an ellipsoid, homeomorphic to $S^2$.
    <2>3. Compute the intersection $A = Y \cap Z$:
        - Subtracting the equations: $(x^2 + y^2 + z^2) - (x^2 + y^2 + z^2/4) = 1 - 1 = 0 \implies \frac{3}{4} z^2 = 0 \implies z = 0$.
        - Substituting $z = 0$ gives $x^2 + y^2 = 1$.
        - Thus $A = Y \cap Z = \{(x, y, 0) \in \mathbb{R}^3 \mid x^2 + y^2 = 1\} \cong S^1$ is the equatorial circle.
    <2>4. The intersection $A$ is a deformation retract of an open neighborhood in $Y$ and in $Z$.

<1>2. Mayer–Vietoris sequence setup:
    *Proof:*
    <2>1. Choose open neighborhoods $U \supset Y$ and $V \supset Z$ in $X$ that deformation retract onto $Y$ and $Z$, respectively, with $U \cap V$ deformation retracting onto $A = Y \cap Z \cong S^1$.
    <2>2. The reduced Mayer–Vietoris sequence is:
    $$\cdots \to \tilde{H}_k(A) \xrightarrow{(i_*, j_*)} \tilde{H}_k(Y) \oplus \tilde{H}_k(Z) \to \tilde{H}_k(X) \xrightarrow{\partial} \tilde{H}_{k-1}(A) \to \cdots$$
    <2>3. The known reduced homology groups of the pieces are:
        - $\tilde{H}_k(A) = \tilde{H}_k(S^1) = \begin{cases} \mathbb{Z} & k = 1, \\ 0 & k \ne 1. \end{cases}$
        - $\tilde{H}_k(Y) \oplus \tilde{H}_k(Z) = \tilde{H}_k(S^2) \oplus \tilde{H}_k(S^2) = \begin{cases} \mathbb{Z} \oplus \mathbb{Z} & k = 2, \\ 0 & k \ne 2. \end{cases}$

<1>3. Computation of homology groups:
    *Proof:*
    <2>1. Degree $k = 0$:
        - $X$ is path-connected because $Y$ and $Z$ are path-connected and $Y \cap Z = S^1 \ne \emptyset$.
        - Thus $H_0(X) \cong \mathbb{Z}$.
    <2>2. Degrees $k \ge 3$:
        - For $k \ge 3$, $\tilde{H}_k(Y) \oplus \tilde{H}_k(Z) = 0$ and $\tilde{H}_{k-1}(A) = 0$.
        - By exactness, $0 \to \tilde{H}_k(X) \to 0$, so $H_k(X) = 0$ for all $k \ge 3$.
    <2>3. Degrees $k = 1$ and $k = 2$:
        - The relevant segment of the reduced Mayer–Vietoris sequence is:
        $$0 \to \tilde{H}_2(Y) \oplus \tilde{H}_2(Z) \xrightarrow{\Phi} \tilde{H}_2(X) \xrightarrow{\partial} \tilde{H}_1(A) \xrightarrow{(i_*, j_*)} \tilde{H}_1(Y) \oplus \tilde{H}_1(Z) \to \tilde{H}_1(X) \to \tilde{H}_0(A) = 0.$$
        - Substitute the known groups:
        $$0 \to \mathbb{Z} \oplus \mathbb{Z} \xrightarrow{\Phi} H_2(X) \xrightarrow{\partial} \mathbb{Z} \xrightarrow{(i_*, j_*)} 0 \to H_1(X) \to 0.$$
        - Because $\tilde{H}_1(Y) \oplus \tilde{H}_1(Z) = 0$, the map $(i_*, j_*): \mathbb{Z} \to 0$ is the zero map.
        - Exactness at $H_1(X)$ gives an isomorphism $H_1(X) \cong \operatorname{coker}(i_*, j_*) = \mathbb{Z}$.
        - Exactness at $\mathbb{Z}$ gives $\operatorname{Im}(\partial) = \ker(i_*, j_*) = \mathbb{Z}$, so $\partial$ is surjective.
        - Exactness at $H_2(X)$ gives the short exact sequence:
        $$0 \to \mathbb{Z} \oplus \mathbb{Z} \xrightarrow{\Phi} H_2(X) \xrightarrow{\partial} \mathbb{Z} \to 0.$$
        - Since $\mathbb{Z}$ is free abelian, the sequence splits:
        $$H_2(X) \cong (\mathbb{Z} \oplus \mathbb{Z}) \oplus \mathbb{Z} \cong \mathbb{Z}^3.$$

<1>4. Conclusion:
    *Proof:*
    The integral homology groups of $X$ are:
    $$H_k(X; \mathbb{Z}) \cong \begin{cases} \mathbb{Z} & k = 0, \\ \mathbb{Z} & k = 1, \\ \mathbb{Z}^3 & k = 2, \\ 0 & k \ge 3. \end{cases}$$
:::
