# Algebra Qualifying Exam (August 2017)

Name:

<a id="directions"></a>
## Directions

Justify all the calculations and state the theorems you use in your answers. In multi-part problems, you may assume the result of any part (even if you have not been able to do it) in working on subsequent parts.

<a id="problems"></a>
## Problems

1. **(10 points)** Suppose the group $G$  acts on the set $A$ . Assume this action is faithful (recall that this means that the kernel of the homomorphism from $G$  to $Sym(A)$  which gives the action is trivial) and transitive (for all $a,b$  in $A$ , there exists $g$  in $G$  such that $g\cdot a=b$ ).

1. For $a\in A$ , let $G_{a}$  denote the stabilizer of $a$  in $G$ . Prove that for any $a\in A$ , $\bigcap _{\sigma \in G}\sigma G_{a}\sigma ^{-1}=1$ .
2. Suppose that $G$  is abelian. Prove that $|G|=|A|$ . Deduce that every abelian transitive subgroup of $S_{n}$  has order $n$ .

2. **(15 points)**

1. Classify the abelian groups of order $36$ .

- For the rest of the problem, assume that $G$  is a non-abelian group of order $36$ . (You may assume that the only subgroup of order $12$  in $S_{4}$  is $A_{4}$  and that $A_{4}$  has no subgroup of order $6$ .)

2. Prove that if the 2-Sylow subgroup of $G$  is normal, $G$  has a normal subgroup $N$  such that $G/N$  is isomorphic to $A_{4}$ .
3. Show that if $G$  has a normal subgroup $N$  such that $G/N$  is isomorphic to $A_{4}$  and a subgroup $H$  isomorphic to $A_{4}$  it must be the direct product of $N$  and $H$ .
4. Show that the dihedral group of order $36$  is a non-abelian group of order $36$  whose Sylow-2 subgroup is not normal.

3. **(10 points)** Let $F$  be a field. Let $f(x)$  be an irreducible polynomial in $F[x]$  of degree $n$  and let $g(x)$  be any polynomial in $F[x]$ . Let $p(x)$  be an irreducible factor (of degree $m$ ) of the polynomial $f(g(x))$ . Prove that $n$  divides $m$ . Use this to prove that if $r$  is an integer which is not a perfect square, and $n$  is a positive integer then every irreducible factor of $x^{2n}-r$  over $\mathbb{Q[}x]$  has even degree.
4. **(10 points)**

1. Let $f(x)$  be an irreducible polynomial of degree $4$  in $\mathbb{Q[}x]$  whose splitting field $K$  over $\mathbb{Q}$  has Galois group $G=S_{4}$ . Let $\theta$  be a root of $f(x)$ . Prove that $\mathbb{Q[}\theta ]$  is an extension of $\mathbb{Q}$  of degree $4$  and that there are no intermediate fields between $\mathbb{Q}$  and $\mathbb{Q[}\theta ]$ .
2. Prove that if $K$  is a Galois extension of $\mathbb{Q}$  of degree $4$ , then there is an intermediate subfield between $K$  and $\mathbb{Q}$ .

5. **(10 points)** A ring $R$  is called simple if its only two-sided ideals are $0$  and $R$ .

1. Suppose $R$  is a commutative ring with $1$ . Prove $R$  is simple if and only if $R$  is a field.
2. Let $k$  be a field. Show the ring $M_{n}(k)$ , $n\times n$  matrices with entries in $k$ , is a simple ring.

6. **(15 points)** For a ring $R$ , let $U(R)$  denote the multiplicative group of units in $R$ . Recall that in an integral domain $R$ , $r\in R$  is called irreducible if $r$  is not a unit in $R$ , and the only divisors of $r$  have the form $ru$  with $u$  a unit in $R$ . We call a non-zero, non-unit $r\in R$  prime in $R$  if $r\mid ab$  implies $r\mid a$  or $r\mid b$ . Consider the ring $R=\{a+b\sqrt{-5}\mid a,b\mathbb{\in Z\}}$ .

1. Prove $R$  is an integral domain.
2. Show $U(R)=\{\pm 1\}$ .
3. Show $3$ , $2+\sqrt{-5}$ , and $2-\sqrt{-5}$  are irreducible in $R$ .
4. Show $3$  is not prime in $R$ .
5. Conclude $R$  is not a PID.

7. **(15 points)** Let $F$  be a field and let $V$  and $W$  be vector spaces over $F$ . Make $V$  and $W$  into $F[X]$ -modules via linear operators $T$  on $V$  and $S$  on $W$  by defining $X\cdot v=T(v)$  for all $v\in V$  and $X\cdot w=S(w)$  for all $w\in W$ . Denote the resulting $F[X]$ -modules by $V_{T}$  and $W_{S}$  respectively.

1. Show that an $F[X]$ -module homomorphism from $V_{T}$  to $W_{S}$  consists of an $F$ -linear transformation $R:V\rightarrow W$  such that $RT=SR$ .
2. Show that $V_{T}\cong W_{S}$  as $F[X]$ -modules if and only if there is an $F$ -linear isomorphism $P:V\rightarrow W$  such that $T=P^{-1}SP$ .
3. Recall that a module $M$  is simple if $M\ne 0$  and any proper submodule of $M$  must be zero. Suppose that $V$  has dimension $2$ . Give an example of $F$ , $T$  with $V_{T}$  simple.
4. Assume $F$  is algebraically closed. Prove that if $V$  has dimension $2$ , then any $V_{T}$  is not simple.