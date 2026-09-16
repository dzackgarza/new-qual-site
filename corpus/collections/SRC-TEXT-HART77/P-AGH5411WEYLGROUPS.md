---
schema: qual/card@1
id: P-AGH5411WEYLGROUPS
kind: problem
title: Weyl groups and the automorphisms of the configuration of 27 lines
classification:
  areas:
  - algebraic-geometry
  topics:
  - Cubic Surfaces
  - Picard Group
  - Intersection Theory
relations: []
review: draft
---

::: problem
Given any diagram consisting of points and line segments joining some of them, we define an abstract group, given by generators and relations, as follows:

- Each point represents a generator $x_i$. The relations are
- $x_i^2=1$ for each $i$;
- $\left(x_i x_j\right)^2=1$ if $i$ and $j$ are not joined by a line segment, and
- $\left(x_i x_j\right)^3=1$ if $i$ and $j$ are joined by a line segment.

a. The Weyl group $\mathbf{A}_n$ is defined using the diagram of $n-1$ points, each joined to the next:

    \begin{tikzcd}
    	\circ & \circ & \cdots & \circ
    	\arrow[dash, from=1-1, to=1-2]
    	\arrow[dash, from=1-2, to=1-3]
    	\arrow[dash, from=1-3, to=1-4]
    \end{tikzcd}

    Show that it is isomorphic to the symmetric group $\Sigma_n$ as follows:
    - Map the generators of $\mathbf{A}_n$ to the elements $(12),(23), \ldots, (n-1,n)$ of $\Sigma_n$, to get a surjective homomorphism $\mathbf{A}_n \rightarrow \Sigma_n$.
    - Then estimate the number of elements of $\mathbf{A}_n$ to show in fact it is an isomorphism.

b. The Weyl group $\mathbf{E}_6$ is defined using the diagram

    \begin{tikzcd}
    	\circ & \circ & \circ & \circ & \circ \\
    	&& \circ
    	\arrow[dash, from=1-1, to=1-2]
    	\arrow[dash, from=1-2, to=1-3]
    	\arrow[dash, from=1-3, to=1-4]
    	\arrow[dash, from=1-4, to=1-5]
    	\arrow[dash, from=1-3, to=2-3]
    \end{tikzcd}

    Call the generators $x_1, \ldots, x_5$ and $y$. Show that one obtains a surjective homomorphism $\mathbf{E}_6 \rightarrow G$, the group of automorphisms of the configuration of 27 lines $(4.10.1)$, by sending $x_1, \ldots, x_5$ to the permutations $(12),(23), \ldots,(56)$ of the $E_i$, respectively, and $y$ to the element associated with the quadratic transformation based at $P_1, P_2, P_3$.

c. Estimate the number of elements in $\mathbf{E}_6$, and thus conclude that $\mathbf{E}_6 \cong G$.

Note: See Manin $[3, \S 25,26]$ for more about Weyl groups, root systems, and exceptional curves.
:::
