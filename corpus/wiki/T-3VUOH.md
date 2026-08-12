---
schema: qual/card@1
id: T-3VUOH
kind: theorem
title: "Mayer-Vietoris"
classification:
  areas:
  - topology
  topics: []
relations: []
review: draft
---
:::{.theorem title="Mayer-Vietoris"}
> Mnemonic: $X = A \union B \leadsto (\intersect, \oplus, \union)$

Let $X = A^\circ \union B^\circ$; then there is a SES of chain complexes
\[
0 \to C_{n}(A\intersect B) \mapsvia{x\mapsto (x, -x)} C_{n}(A) \oplus C_{n}(B) \mapsvia{(x, y) \mapsto x+y} C_{n}(A + B) \to 0
\]
where $C_{n}(A+B)$ denotes the chains that are sums of chains in $A$ and chains in $B$.
This yields a LES in homology:
\[
\cdots  H_{n}(A \cap B) \xrightarrow{(i^*,~ j^*)} H_{n}(A) \oplus H_{n}(B) \xrightarrow{l^* - r^*}  H_{n}(X) \xrightarrow{\delta} H_{n-1}(A\cap B)\cdots
\]
where

- $i: A\cap B \hookrightarrow A$ induces $i^*: H_*(A\cap B) \to H_*(A)$

- $j: A\cap B \hookrightarrow B$ induces $j^*: H_*(A\cap B) \to H_*(B)$

- $l: A \hookrightarrow A\cup B$ induces $l^*: H_*(A) \to H_*(X)$

- $r: B \hookrightarrow A\cup B$ induces $r^*: H_*(B) \to H_*(X)$



More explicitly, 

\begin{tikzcd}
 &  &  &  & \cdots \arrow[lllldd, out=0, in=-180, "\delta_{3}"'] 
 \\
 &  &  &  &  
 \\
H_{2}(A\cap B) \arrow[rr] \arrow[rr, "{(i^*, -j^*)_2}"] &  & H_{2} A \oplus H_{2} B \arrow[rr, "(l^* - r^*)_2"] &  & H_{2} (A\cup B) \arrow[lllldd, "\delta_{2}"', out=0, in=-180] 
\\
 &  &  &  &  
 \\
H_{1}(A\cap B) \arrow[rr, "{(i^*, -j^*)_1}"] &  & H_{1} A \oplus H_{1} B \arrow[rr, "(l^*-r^*)_1"] &  & H_{1} (A\cup B) \arrow[lllldd, "\delta_{1}"', out=0, in=-180] 
\\
 &  &  &  &  
 \\
H_{0} (A\cap B) \arrow[rr, "{(i^*, -j^*)_0}"] &  & H_{0} A \oplus H_{0} B \arrow[rr, "(l^* - r^*)_0"] &  & H_{0} (A\cup B) \arrow[lllldd, "\delta_{0}"', out=0, in=-180] 
\\
 &  &  &  &  
 \\
0 &  &  &  &
\end{tikzcd}

The connecting homomorphisms $\delta_{n} :H_{n}(X) \to H_{n-1}(X)$ are defined by taking a class $[\alpha] \in H_{n}(X)$, writing it as an $n$-cycle $z$, then decomposing $z = \sum c_{i}$ where each $c_{i}$ is an $x+y$ chain. Then $\del(c_{i}) = \del(x+y) = 0$, since the boundary of a cycle is zero, so $\del(x) = -\del(y)$. So then just define $\delta([\alpha]) = [\del x] = [-\del y]$.

Handy mnemonic diagram:
\[
\begin{matrix}
 && A\intersect B & \\
&\diagup &  & \diagdown \\
A\union B & & \longleftarrow &  & A \oplus B
\end{matrix}
.\]

:::
