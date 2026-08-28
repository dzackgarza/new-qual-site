---
order: 40
---

# Modules

## Definitions and Basics

[[D-NQZUY]]

[[PR-TAPZF]]

[[FF-UYMWY]]

[[D-JUYFQ]]

[[PR-JBDUI]]

:::{.remark}
Quotients of modules are easier to reason about additively, writing $M/N = \ts{x + N}$ as cosets.
Then $(x + N) + (y + N) = (x+y) + N$ and $(x+N)(y+N) = (xy) + N$.

:::

[[D-CRWZ7]]

[[FD-BVM37]]

[[D-4HEUB]]

[[FD-2EUYX]]

[[FD-GNRTS]]

[[D-HY7UU]]

[[FD-S2W5E]]

## Structure Theorems

[[PR-DJZLY]]

[[PR-RIJSC]]

## Exact Sequences

[[D-BJYH3]]

:::{.remark}
Note that $C\cong B/d_1(A)$ always, but $B$ is not a direct sum of the outer terms unless the sequence splits.

:::

[[D-3JJJN]]

[[PR-OODAV]]

:::{.proof}
Right-splitting implies direct sum:

- Use that $B \subset \ker d_2 + \im s$, writing $b = (b - sd_2(b) ) + sd_2(b)$ and noting
\[
d_2(b - sd_2(b)) = d_2(b) - d_2sd_2(b) = d_2(b) - d_2(b) = 0 
.\]
- Show $\ker d_2 \intersect \im s=0$, writing $b$ with $d_2(b) = 0$ and $b = s(c)$ for some $c$ yields
\[
0 = d_2(b) = d_2s(c) = \id_C(c) = c
.\]

:::

## Free and Projective Modules

[[D-LIEMF]]

:::{.example title="A non-free module"}
$\ZZ/6$ is a $\ZZ\dash$module that is *not* free, since the element \( [3] \) is a torsion element, where \( 2[3] = [6] = [0] \).
This uses the fact that free modules over a PID are torsionfree.

:::

[[D-IGB7I]]

[[FD-CVEAI]]

[[PR-DLPTR]]

[[D-ZJJ7G]]

[[FF-CY5EA]]

[[FD-BPUNZ]] [[FD-U6KUJ]]

[[FD-SK4ON]]

[[PR-4K4XZ]]

:::{.proof title="that free implies torsionfree"}
\envlist

- If $M$ is finitely generated, write $M = \gens{X}$ with $X\da \ts{x_1, \cdots, x_m}$ and $\size X<\infty$ a finite generating set.
- Since $M$ is free, there is some maximal subset of generators $\mcb \da \ts{x_1, \cdots, x_n} \subseteq X$ where $n\leq m$ that is linearly independent.
- Consider $N\leq M$ defined by $\gens{\mcb}$; this is a basis for $N$ and makes $N$ free.
  The claim is now that $M\cong N$, so that any maximal linearly independent subset of generators is all of $X$.
- If $N \not\cong M$, set $\mcb^c \da X\sm \mcb = \ts{x_{n+1}, \cdots, x_m}$ to be all generators for $M$ that the basis $\mcb$ misses.
- Then $\mcb^c \union \ts{x_{j}}$ for any $n+1\leq j \leq m$ has a linear dependence, and $r_j x_j + \sum_{k=1}^n r_n x_n = 0$ for some $r_j\neq 0$ implies $r_j x_j = - \sum_{k=1}^n r_n x_n$.
- Let $r$ be the product of all of the scalars obtained this way, so $r = \prod_{k=n+1}^m r_j$, and consider the submodule $rX \leq N \leq M$.
  We get $rM \leq N \leq M$ since $X$ is a generating set for $M$, so it now suffices to show $rM \cong M$.
- Just define a map $\phi_r: M\surjects rM$ where $m\mapsto rm$, and note $\ker \phi_r =\ts{ m\in M \st rm = 0} = 0$ since $M$ is torsionfree.
  So $M = M/\ker \phi_r \cong rM$.

:::

:::{.example title="A torsionfree module that is not free"}
$\QQ \in \mods{\ZZ}$ is torsionfree, but not free as a \(\ZZ\dash\)module.
This follows because any two elements $a/b, p/q$ are in a single ideal, since taking $d\da \gcd(b, q)$ we have $1/a = 1/d + \cdots 1/d$ and similarly $p/q = 1/a + \cdots + 1/a$, so these are in \( \gens{ 1/d }  \).
So any basis has size one, which would mean $\QQ = \ts{ \pm 1/d, \pm 2/d, \cdots }$ which in particular doesn't include the average of the first two terms.

:::

[[D-RHJMK]]

[[FD-6XJ7D]]

:::{.remark}
There is a nice way to remember the right diagrams for injective and projective modules.
The slogan is that morphisms *out* of a projective module can be *pulled* back through epimorphisms/surjections, and morphisms *into* an injective module can be *pushed* forward through monomorphisms/injections.

\begin{tikzcd}
	&&&&&& P \\
	\\
	0 && A && B && C && 0 \\
	\\
	&& I
	\arrow[from=3-1, to=3-3]
	\arrow[hook, from=3-3, to=3-5]
	\arrow[two heads, from=3-5, to=3-7]
	\arrow[from=3-7, to=3-9]
	\arrow["{\text{Pull back through surjection}}"', dashed, from=1-7, to=3-5]
	\arrow["{\text{Push forward through injections}}", dashed, from=3-5, to=5-3]
	\arrow[from=1-7, to=3-7]
	\arrow[from=3-3, to=5-3]
\end{tikzcd}

> [Link to Diagram](https://q.uiver.app/?q=WzAsNyxbMCwyLCIwIl0sWzIsMiwiQSJdLFs0LDIsIkIiXSxbNiwyLCJDIl0sWzgsMiwiMCJdLFs2LDAsIlAiXSxbMiw0LCJJIl0sWzAsMV0sWzEsMiwiIiwwLHsic3R5bGUiOnsidGFpbCI6eyJuYW1lIjoiaG9vayIsInNpZGUiOiJ0b3AifX19XSxbMiwzLCIiLDAseyJzdHlsZSI6eyJoZWFkIjp7Im5hbWUiOiJlcGkifX19XSxbMyw0XSxbNSwyLCJcXHRleHR7UHVsbCBiYWNrIHRocm91Z2ggc3VyamVjdGlvbn0iLDIseyJzdHlsZSI6eyJib2R5Ijp7Im5hbWUiOiJkYXNoZWQifX19XSxbMiw2LCJcXHRleHR7UHVzaCBmb3J3YXJkIHRocm91Z2ggaW5qZWN0aW9uc30iLDAseyJzdHlsZSI6eyJib2R5Ijp7Im5hbWUiOiJkYXNoZWQifX19XSxbNSwzXSxbMSw2XV0=)

:::

[[PR-RPL4Q]]

:::{.proof}
\envlist

- Let $M$ be free, so that the universal property gives us this diagram:

\begin{tikzcd}
	M \\
	\\
	{\mathcal{B}} && N
	\arrow["f", from=3-1, to=3-3]
	\arrow["{\tilde f}", dashed, from=1-1, to=3-3]
	\arrow["\iota", hook, from=3-1, to=1-1]
\end{tikzcd}

> [Link to Diagram](https://q.uiver.app/?q=WzAsMyxbMCwyLCJcXG1hdGhjYWx7Qn0iXSxbMCwwLCJNIl0sWzIsMiwiTiJdLFswLDIsImYiXSxbMSwyLCJcXHRpbGRlIGYiLDAseyJzdHlsZSI6eyJib2R5Ijp7Im5hbWUiOiJkYXNoZWQifX19XSxbMCwxLCJcXGlvdGEiLDAseyJzdHlsZSI6eyJ0YWlsIjp7Im5hbWUiOiJob29rIiwic2lkZSI6InRvcCJ9fX1dXQ==)

- To show $M$ is projective, we need to produce a lift in the following diagram, where $B, C$ are arbitrary:

\begin{tikzcd}
	&& M \\
	\\
	B && C && 0
	\arrow[from=3-3, to=3-5]
	\arrow["f", from=1-3, to=3-3]
	\arrow["{\exists \tilde f}"', dashed, from=1-3, to=3-1]
	\arrow["g", two heads, from=3-1, to=3-3]
\end{tikzcd}

> [Link to Diagram](https://q.uiver.app/?q=WzAsNCxbMiwwLCJQIl0sWzIsMiwiQyJdLFswLDIsIkIiXSxbNCwyLCIwIl0sWzEsM10sWzAsMSwiZiJdLFswLDIsIlxcZXhpc3RzIFxcdGlsZGUgZiIsMix7InN0eWxlIjp7ImJvZHkiOnsibmFtZSI6ImRhc2hlZCJ9fX1dLFsyLDEsImciLDAseyJzdHlsZSI6eyJoZWFkIjp7Im5hbWUiOiJlcGkifX19XV0=)

- It suffices to produce a map $\mathcal{B}\to B$, since the universal property then provides $M\to B$.
  Here's the schematic:  

\begin{tikzcd}
	&& {\mathcal{B}} & {\ts{e_i}} \\
	\\
	&& M \\
	\\
	B && C && 0 \\
	{\ts{g\inv f(e_i)}} && {} & {\ts{f(e_i)}}
	\arrow[from=5-3, to=5-5]
	\arrow["f", from=3-3, to=5-3]
	\arrow["{\exists \tilde f}"', dashed, from=3-3, to=5-1]
	\arrow["g", two heads, from=5-1, to=5-3]
	\arrow[hook, from=1-3, to=3-3]
	\arrow[dotted, maps to, from=1-4, to=6-4]
	\arrow[dotted, maps to, from=6-4, to=6-1]
\end{tikzcd}

> [Link to Diagram](https://q.uiver.app/?q=WzAsOSxbMiwyLCJNIl0sWzIsNCwiQyJdLFswLDQsIkIiXSxbNCw0LCIwIl0sWzIsMCwiXFxtYXRoY2Fse0J9Il0sWzMsMCwiXFx0c3tlX2l9Il0sWzIsNV0sWzMsNSwiXFx0c3tmKGVfaSl9Il0sWzAsNSwiXFx0c3tnXFxpbnYgZihlX2kpfSJdLFsxLDNdLFswLDEsImYiXSxbMCwyLCJcXGV4aXN0cyBcXHRpbGRlIGYiLDIseyJzdHlsZSI6eyJib2R5Ijp7Im5hbWUiOiJkYXNoZWQifX19XSxbMiwxLCJnIiwwLHsic3R5bGUiOnsiaGVhZCI6eyJuYW1lIjoiZXBpIn19fV0sWzQsMCwiIiwwLHsic3R5bGUiOnsidGFpbCI6eyJuYW1lIjoiaG9vayIsInNpZGUiOiJ0b3AifX19XSxbNSw3LCIiLDAseyJzdHlsZSI6eyJ0YWlsIjp7Im5hbWUiOiJtYXBzIHRvIn0sImJvZHkiOnsibmFtZSI6ImRvdHRlZCJ9fX1dLFs3LDgsIiIsMCx7InN0eWxlIjp7InRhaWwiOnsibmFtZSI6Im1hcHMgdG8ifSwiYm9keSI6eyJuYW1lIjoiZG90dGVkIn19fV1d)

- Here we write $\mcb \da \ts{e_i}$, included into $M$, and mapped by $f$ to $C$.
  Then use surjectivity to choose preimages in $B$ under $g$ arbitrarily, and this defines a morphism $\mcb \to B$.

:::

:::{.example title="Projective $\not\implies$ free"}
Let \( R_1, R_2 \) be two nontrivial rings and set \( R \da R_1 \oplus R_2 \).
Then \( R_1, R_2 \) are projective \( R\dash \)modules by construction, but each factor contains \( R\dash \)torsion:
setting \( e \da (0, 1) \in R \) we have \( e \actson R_1 = 0_{R_1} \).
Since free implies torsionfree, \( R_1 \) can not be a free \(R\dash\)module.

:::

## Classification of Modules over a PID

[[PR-UVUS6]]

[[FD-LHLDU]]

[[PR-ASW5L]]

:::{.proof}
$\implies$:

Suppose $I$ is free as an $R\dash$module, and let $B = \theset{\vector m_j}_{j\in J} \subseteq I$ be a basis so we can write $M = \generators{B}$.
Suppose that $\abs{B} \geq 2$, so we can pick at least 2 basis elements $\vector m_1\neq \vector m_2$, and consider
$$
\vector c = \vector m_1 \vector m_2 - \vector m_2 \vector m_1,
$$

which is also an element of $M$ .
Since $R$ is an integral domain, $R$ is commutative, and so
$$
\vector c = \vector m_1 \vector m_2 - \vector m_2 \vector m_1 = \vector m_1 \vector m_2 - \vector m_1 \vector m_2 = \vector 0_M
$$

However, this exhibits a linear dependence between $\vector m_1$ and $\vector m_2$, namely that there exist $\alpha_1, \alpha_2 \neq 0_R$ such that $\alpha_1 \vector m_1 + \alpha_2 \vector m_2 = \vector 0_M$; this follows because $M \subset R$ means that we can take $\alpha_1 = -m_2, \alpha_2 = m_1$. This contradicts the assumption that $B$ was a basis, so we must have $\abs{B} = 1$ and so $B = \theset{\vector m}$ for some $\vector m \in I$. But then $M = \generators{B} = \generators{\vector m}$ is generated by a single element, so $M$ is principal.

$\impliedby$:
Suppose $M\normal R$ is principal, so $M = \generators{\vector m}$ for some $\vector m \neq \vector{0}_M \in M \subset R$.

Then $x\in M \implies x = \alpha\vector m$ for some element $\alpha\in R$ and we just need to show that $\alpha\vector m = \vector 0_M \implies \alpha = 0_R$ in order for $\theset{\vector m}$ to be a basis for $M$, making $M$ a free $R\dash$module.
But since $M \subset R$, we have $\alpha, m \in R$ and $\vector 0_M = 0_R$, and since $R$ is an integral domain, we have $\alpha m = 0_R \implies \alpha = 0_R$ or $m = 0_R$.
Since $m \neq 0_R$, this forces $\alpha = 0_R$, which allows $\theset{m}$ to be a linearly independent set and thus a basis for $M$ as an $R\dash$module.

:::

:::{.remark}
This says every module $M$ decomposes as $M \cong F_M \oplus M_t$ where $F_M$ is free (and thus torsionfree) and $M_t$ is torsion, and moreover $F_M \cong M/M_t$.

That $M/M_t$ is torsionfree: suppose $r(m+ M_t) = M_t$, so $rm\in M_t$ is torsion.
Then $r'(rm)=0$ for some $r'$, making $m$ torsion, and $m+ M_t = M_t$ is the zero coset.

That $F_M \cong M/M_t$: take the SES $0\to M_t\to M \to F\to 0$ to get $F\cong M/M_t$.
This splits since $F$ is free and thus projective, so $F\cong M \oplus M_t$.

:::

## Algebraic Properties

[[D-B5X33]]

[[PR-O5YUI]]
[[PR-BHUO6]]
[[PR-TGFTL]]

[[PR-LPJLD]]

[[PR-5PDNQ]]

[[PR-GXII2]]

[[PR-KX7L7]]

:::{.example title="Computing tensor products"}
$\ZZ/2 \tensor_\ZZ \ZZ/3 = 0$:

\begin{tikzcd}
	0 && {\ZZ \tensor_\ZZ \ZZ/3} && {\ZZ \tensor_\ZZ \ZZ/3} && {\ZZ/3 \tensor_\ZZ \ZZ/2} \\
	\\
	0 && {\ZZ/3} && {\ZZ/3} && 0
	\arrow["{(\wait \times 2)}", from=3-3, to=3-5]
	\arrow["{(\wait \times 2) \cross \one}", from=1-3, to=1-5]
	\arrow[from=3-5, to=3-7]
	\arrow[from=1-5, to=1-7]
	\arrow[from=1-1, to=1-3]
	\arrow[from=3-1, to=3-3]
	\arrow["{\proj_2}"{description}, from=1-3, to=3-3]
	\arrow["{\proj_2}"{description}, from=1-5, to=3-5]
	\arrow["\cong", dashed, from=1-7, to=3-7]
\end{tikzcd}

> [Link to Diagram](https://q.uiver.app/?q=WzAsOCxbMiwwLCJcXFpaIFxcdGVuc29yX1xcWlogXFxaWi8zIl0sWzQsMCwiXFxaWiBcXHRlbnNvcl9cXFpaIFxcWlovMyJdLFsyLDIsIlxcWlovMyJdLFs0LDIsIlxcWlovMyJdLFs2LDIsIjAiXSxbNiwwLCJcXFpaLzMgXFx0ZW5zb3JfXFxaWiBcXFpaLzIiXSxbMCwyLCIwIl0sWzAsMCwiMCJdLFsyLDMsIihcXHdhaXQgXFx0aW1lcyAyKSJdLFswLDEsIihcXHdhaXQgXFx0aW1lcyAyKSBcXGNyb3NzIFxcb25lIl0sWzMsNF0sWzEsNV0sWzcsMF0sWzYsMl0sWzAsMiwiXFxwcm9qXzIiLDFdLFsxLDMsIlxccHJval8yIiwxXSxbNSw0LCJcXGNvbmciLDAseyJzdHlsZSI6eyJib2R5Ijp7Im5hbWUiOiJkYXNoZWQifX19XV0=)

:::
