---
title: Counterexamples
order: 9
topics:
- Counterexamples
---

# Counterexamples

## Groups

**Converse of Lagrange's theorem.** A finite group need not have a subgroup of each order dividing its order.
The [[D-TMME3|alternating group]] $A_4$ has order $12$ and no subgroup of order $6$; $A_5$ has order $60$ and no subgroup of order $30$.

**Groups of order $p^3$.** A group of order $p^3$ need not be abelian: the [[D-4R2Z5|dihedral group]] $D_4$ and the [[D-KRKV7|quaternion group]] $Q_8$ have order $8$.
Every group of order $p^2$ is abelian.

**Groups whose proper subgroups are abelian.** $A_4$ is nonabelian, and each of its proper subgroups has order $1$, $2$, $3$, or $4$, hence is abelian.

**Transitivity of normality.** In $A_4$, $\langle (1\,2)(3\,4)\rangle \normal V_4$ and $V_4 \normal A_4$, but $\langle (1\,2)(3\,4)\rangle$ is not a [[D-EKE4Q|normal subgroup]] of $A_4$.

**Quotients embedding as subgroups.** A quotient of $G$ need not be isomorphic to a subgroup of $G$.
The quotient $Q_8/\{\pm 1\}\cong \ZZ/2\times\ZZ/2$ does not embed in $Q_8$, whose only element of order $2$ is $-1$; the quotient $\ZZ/2$ of $\ZZ$ does not embed in $\ZZ$.
For a finite abelian group every quotient is isomorphic to a subgroup.

## Rings

The classes of rings, each with a ring separating it from the next, are on [[algebra/rings-and-ideals/which-kind-of-ring|Which kind of ring is this?]].

**Irreducible elements.** An [[D-TO3IY|irreducible element]] need not be [[D-AWSKI|prime]]; in $\ZZ[\sqrt{-5}]$, $3$ is irreducible, and $9 = 3\cdot 3 = (2+\sqrt{-5})(2-\sqrt{-5})$ with $3$ dividing neither factor on the right.

**Subrings of a PID.** A subring of a [[D-HTIL5|principal ideal domain]] need not be one: $\ZZ[x] \subseteq \QQ[x]$.

**Polynomial rings over a PID.** If $R$ is a principal ideal domain, $R[x]$ need not be: the ideal $\gens{2,x}\normal\ZZ[x]$ is not principal.

## Modules

**Torsion-free modules.** A [[D-ZJJ7G|torsion-free]] module over an integral domain need not be [[D-LIEMF|free]]; the ideal $\gens{2,x}\subseteq \ZZ[x]$ is torsion-free and not free.

**Projective modules.** A [[D-RHJMK|projective module]] need not be free: $\ZZ/2$ is a direct summand of $\ZZ/6\cong \ZZ/2\times\ZZ/3$, hence projective over $\ZZ/6$, and it is not free because it has $2$ elements.

**Tensor products and injectivity.** Tensoring need not preserve injective maps: multiplication by $2$ on $\ZZ$ is injective, and tensored with $\ZZ/2$ it is the zero map on $\ZZ/2$.

**Split exact sequences.** An [[D-BJYH3|exact sequence]] need not [[D-3JJJN|split]]; $0\to\ZZ/2\to\ZZ/4\to\ZZ/2\to 0$, since $\ZZ/4\not\cong \ZZ/2\times\ZZ/2$.

## Linear algebra

Further matrix counterexamples are on [[algebra/linear-algebra/matrix-counterexamples|Matrix counterexamples]].

**Characteristic polynomials and similarity.** Matrices with the same [[D-QFYAC|characteristic polynomial]] and the same [[D-GK5SF|minimal polynomial]] need not be [[D-JIGMN|similar]]; $J_2(0)\oplus J_2(0)$ and $J_2(0)\oplus J_1(0) \oplus J_1(0)$ both have characteristic polynomial $x^4$ and minimal polynomial $x^2$.

**Real eigenvalues.** A real matrix need not have a real eigenvalue: the rotation $\begin{pmatrix}0&-1\\1&0\end{pmatrix}$ has characteristic polynomial $x^2+1$.

**Diagonalizability over $\RR$ and $\CC$.** The same rotation is diagonalizable over $\CC$, with eigenvalues $\pm i$, and not over $\RR$.

## Fields

**Normal extensions.** A finite extension need not be [[D-LZTAK|normal]]; $\QQ(2^{1/3})/\QQ$, since $x^3-2$ has one root in $\QQ(2^{1/3})\subseteq\RR$.

**Transitivity of normality.** $\QQ(2^{1/4})/\QQ(\sqrt2)$ and $\QQ(\sqrt2)/\QQ$ are normal, being of degree $2$, but $\QQ(2^{1/4})/\QQ$ is not.

**Separability.** An irreducible polynomial need not be [[D-ZT46D|separable]]; $x^p - t$ over $\FF_p(t)$ is irreducible and equals $(x-t^{1/p})^p$ over a splitting field.
Every irreducible polynomial over a [[D-KQFIV|perfect field]], in particular over a field of characteristic zero or a finite field, is separable.

**Simple extensions.** A finite extension need not be [[D-PUOGJ|simple]]; $\FF_p(s,t)/\FF_p(s^p,t^p)$ has degree $p^2$, and every element $\alpha$ of $\FF_p(s,t)$ satisfies $\alpha^p\in\FF_p(s^p,t^p)$, so every simple subextension has degree at most $p$.
By the primitive element theorem, every finite separable extension is simple.
