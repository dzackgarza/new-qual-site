---
schema: qual/card@1
id: P-ULHPN
kind: problem
title: "Compute $\\ext(\\ZZ \\oplus \\ZZ/2 \\oplus \\ZZ/3, \\ZZ \\oplus \\ZZ/4 \\oplus \\ZZ/5)$. Facts Used: Since $\\ZZ$ is a free $\\ZZ\\dash$module, $\\ext(\\ZZ, \\ZZ/m) = 0$"
classification:
  areas:
  - topology
  topics:
  - homological-algebra
relations: []
review: draft
solved: true
---
Compute $\ext(\ZZ \oplus \ZZ/2 \oplus  \ZZ/3, \ZZ \oplus  \ZZ/4 \oplus  \ZZ/5)$.

:::{.solution}


\envlist
:::{.concept}
\envlist
Facts Used:[^fix_facts_on_ext_oskar]

- Since $\ZZ$ is a free $\ZZ\dash$module,
\[
\ext(\ZZ, \ZZ/m) = 0
\]

- Using the usual projective resolution $0 \to \ZZ \to \ZZ \to \ZZ/n \to 0$, 
\[
\ext(\ZZ/n, \ZZ) = \ZZ/n
.\]

- 
\[
\ext(\ZZ/n, \ZZ/m) = (\ZZ/m) / (n \cdot \ZZ/m) \cong (\ZZ/m) / (d \cdot \ZZ/m) && 
\\ \text{where } d \da \gcd(m, n)
.\]
  General principle: $\Ext(\ZZ/n, G) = G/nG$ 

  By applying $\Hom_\ZZ(\wait, G)$ to the above resolution: 

\begin{tikzcd}
	& 0 & {\Ext^1_\ZZ(\ZZ/n, G)} \\
	\\
	{\Hom_\ZZ(\ZZ, G)} & {\Hom_\ZZ(\ZZ, G)} & {\Hom_\ZZ(\ZZ/n, G)} & 0 \\
	&&& {}
	\arrow[hook', from=3-3, to=3-2]
	\arrow["{\cdot n}"', from=3-2, to=3-1]
	\arrow[two heads, from=3-1, to=1-3, out=180, in=360]
	\arrow[from=1-3, to=1-2]
	\arrow[from=3-4, to=3-3]
\end{tikzcd}

  > [Link to Diagram](https://q.uiver.app/?q=WzAsNyxbMiwwLCIwIl0sWzAsMiwiXFxIb21fXFxaWihcXFpaLCBHKSJdLFsyLDIsIlxcSG9tX1xcWlooXFxaWiwgRykiXSxbNCwyLCJcXEhvbV9cXFpaKFxcWlovbiwgRykiXSxbNCwwLCJcXEV4dF4xX1xcWlooXFxaWi9uLCBHKSJdLFs2LDIsIjAiXSxbNCwzXSxbMywyLCIiLDIseyJzdHlsZSI6eyJ0YWlsIjp7Im5hbWUiOiJob29rIiwic2lkZSI6ImJvdHRvbSJ9fX1dLFsyLDEsIlxcY2RvdCBuIiwyXSxbMSw0LCIiLDAseyJzdHlsZSI6eyJoZWFkIjp7Im5hbWUiOiJlcGkifX19XSxbNCwwXSxbNSwzXV0=)

  which can be identified with:

\begin{tikzcd}
	&& 0 && {G/nG} \\
	\\
	G && G && {\Hom_\ZZ(\ZZ/n, G)} && 0 \\
	&&&& {}
	\arrow[hook', from=3-5, to=3-3]
	\arrow["{\cdot n}"', from=3-3, to=3-1]
	\arrow[two heads, from=3-1, to=1-5, out=180, in=360]
	\arrow[from=1-5, to=1-3]
	\arrow[from=3-7, to=3-5]
\end{tikzcd}

  > [Link to Diagram](https://q.uiver.app/?q=WzAsNyxbMiwwLCIwIl0sWzAsMiwiRyJdLFsyLDIsIkciXSxbNCwyLCJcXEhvbV9cXFpaKFxcWlovbiwgRykiXSxbNCwwLCJHL25HIl0sWzYsMiwiMCJdLFs0LDNdLFszLDIsIiIsMix7InN0eWxlIjp7InRhaWwiOnsibmFtZSI6Imhvb2siLCJzaWRlIjoiYm90dG9tIn19fV0sWzIsMSwiXFxjZG90IG4iLDJdLFsxLDQsIiIsMCx7InN0eWxlIjp7ImhlYWQiOnsibmFtZSI6ImVwaSJ9fX1dLFs0LDBdLFs1LDNdXQ==)

3. Contravariant Hom takes coproducts to products:
\[
\ext(\bigoplus_{i\in I} A_i, \prod_{k\in K} B_k) = \prod_{i\in I} \prod_{k\in K} \ext(A_i, B_k)
.\]

:::


Write 
\[
A_\wait &\da A_1 \oplus A_2 \oplus A_3 \da \ZZ \oplus  \ZZ/2 \oplus  \ZZ/3 \\
B_\wait &\da B_1 \oplus B_2 \oplus B_3 \da \ZZ \oplus \ZZ/4 \oplus  \ZZ/5
.\]

We can then define the bicomplex \[
C_{\wait, \wait} \da \Ext(A_\wait, B_\wait) = \bigoplus_{0 \leq i, k \leq 3} \Ext(A_i, B_k)
,\]
i.e. $C_{i, k} \da \Ext(A_i, B_k)$, which can be organized into the following diagram where we take the Ext at each position and sum them all together:

\begin{tikzcd}
	{\Ext(A_1, B_1)} && {\Ext(A_1, B_2)} && {\Ext(A_1, B_3)} \\
	\\
	{\Ext(A_2, B_1)} && {\Ext(A_2, B_2)} && {\Ext(A_2, B_3)} \\
	\\
	{\Ext(A_3, B_1)} && {\Ext(A_3, B_2)} && {\Ext(A_3, B_3)}
\end{tikzcd}

> [Link to Diagram](https://q.uiver.app/?q=WzAsOSxbMCwwLCJcXEV4dF8xXlxcWlooQV8xLCBCXzEpIl0sWzAsMiwiXFxFeHRfMV5cXFpaKEFfMiwgQl8xKSJdLFswLDQsIlxcRXh0XzFeXFxaWihBXzMsIEJfMSkiXSxbMiwwLCJcXEV4dF8xXlxcWlooQV8xLCBCXzIpIl0sWzQsMCwiXFxFeHRfMV5cXFpaKEFfMSwgQl8zKSJdLFsyLDIsIlxcRXh0XzFeXFxaWihBXzIsIEJfMikiXSxbNCwyLCJcXEV4dF8xXlxcWlooQV8yLCBCXzMpIl0sWzIsNCwiXFxFeHRfMV5cXFpaKEFfMywgQl8yKSJdLFs0LDQsIlxcRXh0XzFeXFxaWihBXzMsIEJfMykiXV0=)

This equals the following:

\begin{tikzcd}
	{\Ext(\ZZ, \ZZ)} && {\Ext(\ZZ, \ZZ/4)} && {\Ext(\ZZ, \ZZ/5)} \\
	\\
	{\Ext(\ZZ/2, \ZZ)} && {\Ext(\ZZ/2, \ZZ/4)} && {\Ext(\ZZ/2, \ZZ/5)} \\
	\\
	{\Ext(\ZZ/3, \ZZ)} && {\Ext(\ZZ/3, \ZZ/4)} && {\Ext(\ZZ/3, \ZZ/5)}
\end{tikzcd}

> [Link to Diagram](https://q.uiver.app/?q=WzAsOSxbMCwwLCJcXEV4dF8xXlxcWlooQV8xLCBCXzEpIl0sWzAsMiwiXFxFeHRfMV5cXFpaKEFfMiwgQl8xKSJdLFswLDQsIlxcRXh0XzFeXFxaWihBXzMsIEJfMSkiXSxbMiwwLCJcXEV4dF8xXlxcWlooQV8xLCBCXzIpIl0sWzQsMCwiXFxFeHRfMV5cXFpaKEFfMSwgQl8zKSJdLFsyLDIsIlxcRXh0XzFeXFxaWihBXzIsIEJfMikiXSxbNCwyLCJcXEV4dF8xXlxcWlooQV8yLCBCXzMpIl0sWzIsNCwiXFxFeHRfMV5cXFpaKEFfMywgQl8yKSJdLFs0LDQsIlxcRXh0XzFeXFxaWihBXzMsIEJfMykiXV0=)


Which simplifies to:

\begin{tikzcd}
	0 && 0 && 0 \\
	\\
	{\ZZ/2} && {\ZZ/2} && 0 \\
	\\
	{\ZZ/3} && {0} && {0}
\end{tikzcd}


> [Link to Diagram](https://q.uiver.app/?q=WzAsOSxbMCwwLCJcXEV4dF8xXlxcWlooQV8xLCBCXzEpIl0sWzAsMiwiXFxFeHRfMV5cXFpaKEFfMiwgQl8xKSJdLFswLDQsIlxcRXh0XzFeXFxaWihBXzMsIEJfMSkiXSxbMiwwLCJcXEV4dF8xXlxcWlooQV8xLCBCXzIpIl0sWzQsMCwiXFxFeHRfMV5cXFpaKEFfMSwgQl8zKSJdLFsyLDIsIlxcRXh0XzFeXFxaWihBXzIsIEJfMikiXSxbNCwyLCJcXEV4dF8xXlxcWlooQV8yLCBCXzMpIl0sWzIsNCwiXFxFeHRfMV5cXFpaKEFfMywgQl8yKSJdLFs0LDQsIlxcRXh0XzFeXFxaWihBXzMsIEJfMykiXV0=)

So the answer is $\ZZ/2 \oplus \ZZ/2 \oplus \ZZ/3 \cong \ZZ/2 \oplus \ZZ/6$. 

[^fix_facts_on_ext_oskar]: 
Thanks to Oskar Henriksson for some fixes/clarifications and further explanations here!

:::
