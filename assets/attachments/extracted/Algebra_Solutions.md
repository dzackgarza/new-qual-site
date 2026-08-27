Kleshchev Algebra
Student Solution Manual
Chapter 1 through 5
James Wilson
1 Groups
• Sylow Theorems
• Simple Groups
• Chain Conditions
2 Fields
• Galois Theory
• Finite Fields
• Transcendental Extensions
3 Modules
• Over PIDs
• Semi-simplicity
• Algebras
4 Categories
• Commutative Diagrams
• Naturality
• Category Equivalence
5 Commutative Algebra
• Localization/Extensions
• Radicals
• Algebraic Geometry
Published: December 3, 2003

c©2002-2003. James Wilson, University of Oregon.
Department of Mathematics
1222 University of Oregon
Eugene, OR 97403-1222
jwilson7@darkwing.uoregon.edu
www.uoregon.edu/ jwilson7/
Written with LATEX 2ε.
Please Recycle when ﬁnished.
This is the product of a graduate level algebra course taken at the University
of Oregon, 2002-2003, under the instruction of Alexander Kleshchev. The so-
lutions are mostly the work of the author, James Wilson, while the exercises
were developed by Kleshchev. Many exercises appear in common texts, such as
Hungerford’s Algebra and Rotman’s Advanced Modern Algebra.
I developed the solutions as a preparation for the Ph.D. qualifying exams. With
the exception of some parts of chapter 2, most of the solutions have been proof
read to some degree. However, mistakes are bound to exist still. My hope is
that these may help others with many of the common problems encountered
when preparing for qualifying exams. Having passed the exams, my advice in
using these notes is to do each problem yourself.
I welcome any comments and corrections you may have. I would also like to
thank Professor Kleshchev, David Hill, Alex Jordan, and Dragos Neacsu for
their advice on certain solutions.

Contents
1 Groups 5
2 Fields 35
3 Modules 65
4 Categories 125
5 Rings 127
3

4 CONTENTS

Chapter 1
Groups
1 T/F Cyclic Groups . . . . . . . . . . . . . . . . . . . . . . 7
2 Transitive Embedding . . . . . . . . . . . . . . . . . 7
3 Probability of Commutativity . . . . . . . . . . . . . 7
4 Inﬁnite Groups . . . . . . . . . . . . . . . . . . . . . 8
5 Frattini Subgroup . . . . . . . . . . . . . . . . . . . . 8
6 T/F Cyclic Automorphisms . . . . . . . . . . . . . . . . . 8
7 Maximal p-subgroups . . . . . . . . . . . . . . . . . . 9
8 Minimal p-quotients . . . . . . . . . . . . . . . . . . 9
9 T/F Nilpotent Subgroups . . . . . . . . . . . . . . . . . . 10
10 Classiﬁcation of “Local” Groups . . . . . . . . . . . 10
11 p-subgroup Chains . . . . . . . . . . . . . . . . . . . 11
12 T/F Counting Involutions . . . . . . . . . . . . . . . . . . 11
13 Nilpotent Extensions . . . . . . . . . . . . . . . . . . 12
14 T/F Normal Transitivity . . . . . . . . . . . . . . . . . . 12
15 Examples of the Parallelogram Law . . . . . . . . . . 12
16 The Complex Subgroup . . . . . . . . . . . . . . . . 13
17 Parallelogram Law . . . . . . . . . . . . . . . . . . . 13
18 HK -subgroup . . . . . . . . . . . . . . . . . . . . . . 13
19 T/F Hamiltonian Groups . . . . . . . . . . . . . . . . . . 14
20 Center of Sn . . . . . . . . . . . . . . . . . . . . . . . 14
21 Parallelogram Example . . . . . . . . . . . . . . . . . 14
22 Q subgroups . . . . . . . . . . . . . . . . . . . . . . . 15
23 Finite Index Intersections . . . . . . . . . . . . . . . 15
24 Unions of Conjugation . . . . . . . . . . . . . . . . . 15
25 Unions of Conjugation . . . . . . . . . . . . . . . . . 16
26 Conjugacy Classes and Generators . . . . . . . . . . 16
27 GLn(Fq) . . . . . . . . . . . . . . . . . . . . . . . . . 16
28 Conjugate Cluster . . . . . . . . . . . . . . . . . . . 17
29 3 Sylow-2-subgroups . . . . . . . . . . . . . . . . . . 17
30 Inﬁnite Simple Groups . . . . . . . . . . . . . . . . . 18
31 Simple Groups of order 120 . . . . . . . . . . . . . . 18
32 Simple Groups of order 2 472 . . . . . . . . . . . . . . 18
33 Simple Groups of order 150 . . . . . . . . . . . . . . 18
34 Simple Groups of order 80. . . . . . . . . . . . . . . 18
35 D8 Representation . . . . . . . . . . . . . . . . . . . 19
36 Trivial Relations . . . . . . . . . . . . . . . . . . . . 19
37 2 Conjugacy Classes . . . . . . . . . . . . . . . . . . 19
5

6 CHAPTER 1. GROUPS
38 T/F S4 . . . . . . . . . . . . . . . . . . . . . . . . . . . . 20
39 T/F Transitive Subgroups of S5 . . . . . . . . . . . . . . 20
40 T/F pq-groups . . . . . . . . . . . . . . . . . . . . . . . . 20
41 Metabelian . . . . . . . . . . . . . . . . . . . . . . . 20
42 T/F Normalizers of Sylow subgroups . . . . . . . . . . . . 21
43 Inherited Sylow subgroups . . . . . . . . . . . . . . . 21
44 Normalizers of Sylow-subgroups. . . . . . . . . . . . 21
45 Simple Groups of Order pqr. . . . . . . . . . . . . . . 21
46 Simple Groups of Order p(p + 1). . . . . . . . . . . . 22
47 Cyclic Sylow-2-subgroups. . . . . . . . . . . . . . . . 22
48 Automorphism of Sn. . . . . . . . . . . . . . . . . . . 23
49 Automorphism of S6. . . . . . . . . . . . . . . . . . . 23
50 Nilpotency and Normalizers. . . . . . . . . . . . . . . 23
51 T/F Dihedral Nilpotency. . . . . . . . . . . . . . . . . . . 23
52 Sylow-subgroups of Quotients. . . . . . . . . . . . . . 24
53 Sylow-subgroups of Normal subgroups. . . . . . . . . 24
54 Conjugacy Classes. . . . . . . . . . . . . . . . . . . . 24
55 Embedding in An. . . . . . . . . . . . . . . . . . . . 25
56 T/F C15 as a Permutation Group. . . . . . . . . . . . . . 25
57 C15 as a Permutation Group. . . . . . . . . . . . . . 25
58 T/F Normal Sylow-subgroups. . . . . . . . . . . . . . . . 25
59 Centers of p-groups. . . . . . . . . . . . . . . . . . . 25
60 Centers. . . . . . . . . . . . . . . . . . . . . . . . . . 26
61 Centers of Products. . . . . . . . . . . . . . . . . . . 26
62 T/F Counter Examples. . . . . . . . . . . . . . . . . . . . 26
63 Solvable Groups. . . . . . . . . . . . . . . . . . . . . 27
64 Subgroups of Cp ×Cp. . . . . . . . . . . . . . . . . . 27
65 Automorphisms. . . . . . . . . . . . . . . . . . . . . 27
66 T/F Nilpotency of order 18. . . . . . . . . . . . . . . . . . 28
67 Diagonal Embedding. . . . . . . . . . . . . . . . . . . 28
68 T/F Centrality in p-groups. . . . . . . . . . . . . . . . . . 28
69 Classiﬁcation of Sylow-subgroups. . . . . . . . . . . . 28
70 Groups of order 175. . . . . . . . . . . . . . . . . . . 28
71 Free-Abelian Groups. . . . . . . . . . . . . . . . . . . 29
72 Free Groups. . . . . . . . . . . . . . . . . . . . . . . 29
73 Symmetries of the Tetrahedron. . . . . . . . . . . . . 29
74 Conjugation in S5. . . . . . . . . . . . . . . . . . . . 30
75 T/F Dihedral Groups. . . . . . . . . . . . . . . . . . . . . 31
76 Sp generators. . . . . . . . . . . . . . . . . . . . . . . 31
77 Dihedral Groups. . . . . . . . . . . . . . . . . . . . . 32

Algebra – James Wilson 7
1 Cyclic Groups – True or False? Let G be a group such that any ﬁnitely
generated subgroup of G is cyclic. Then G is cyclic. Hint: Consider the Pr¨ ufer
group Z(p∞).Example: Of course the assertion is too good to be true, and we ﬁnd a counter
example in the Pr¨ ufer group Z(p∞). The geometric description of the Pr¨ ufer
group is the rotations of all pn-gons, for all n ∈ N. These are all inscribed one
in the next. The subgroups, thus, form a chain of cyclic groups, and so any
ﬁnite number of generators is generated by a generator with highest order, that
is, that all ﬁnitely generated subgroups are cyclic. However, the entire group
is not cyclic as certainly it is not isomorphic to Z which has the subgroups 2 Z
and 3 Z which are not in a chain. □
2 Transitive Embedding Let G be a ﬁnite group with |G|>n . Then G is Hint: Consider G acting on
G/H.isomorphic to a transitive subgroup of Sn if and only if G contains a subgroup
H of index n such that neither H nor any proper subgroup of H is normal in
G.
Proof: Suppose H is a subgroup of index n in G which is not normal and
which has no proper normal subgroups. Let us take G to act on the left cosets
G/H. This induces a homomorphism G →Sn whose kernel must be contained
in H (as gH ⁄= H whenever g /∈ H.) However, H is not normal, nor are any
of its proper subgroups, so the only option we have is to choose the kernel as
⟨1⟩. This kernel shows we have a monomorphism so G is represented faithfully
in Sn. Since the action of G on G/H is always transitive, the representation of
G in Sn is transitive.
Now that the mystery is explained we consider the reverse implication. Begin
with G a transitive faithful embedding of G in Sn. Then we must have an
monomorphism G → Sn. This induces a natural action of G on n elements.
This action is G-isomorphic to G acting on G/G1 by [ Kle03, Theorem-1.5.5].
The action is transitive so the size of the orbit is n which forces the size of index
of the stabilizer G1 in G to be n.
All that remains is to show no non-trivial subgroup of G1 is normal in G
– including G1. Suppose there where a normal subgroup N in G contained in
G1. Since G1 is conjugate to Gi for all i = 2,...,n , then in fact N – which is
invariant under conjugation – is in each Gi. However we know the intersection
of all Gi’s is trivial – since it is precisely the kernel of the faithful embedding of
G – and it would certainly contain N ; thus, N must be trivial. □
3 Probability of Commutativity Let G be a ﬁnite group. We choose an Hint: Use Brunside’s
Formula[Rot02, Thm-2.113]
and centralizers.
elementg ∈G randomly, then replace it and make another random choice of an
elementh ∈G. Prove that the probability that g andh commute equals k/|G|,
where k is the number of conjugacy classes in G.
Proof: Given a ﬁxedg ∈G, the probability of choosing an element h ∈G which
commutes with g is the same as the probability of selecting something from the
centralizer, so |CG(g)|/|G|. Since this is for a speciﬁc element we must average
over all the elements. As the group action is conjugation, CG(g) = Fix (g) so
we get:
P = 1
|G|
∑
g∈G
|CG(g)|
|G| = 1
|G|

 1
|G|
∑
g∈G
|Fix (g)|

 = k
|G|.
Notice the second step applies the Burnside’s Lemma [ Rot02, Thm-2.113]. □

8 CHAPTER 1. GROUPS
4 Inﬁnite Groups Any inﬁnite group has inﬁnitely many subgroups.Hint: Show either a subgroup
is a copy of Z, or there are in-
ﬁnitely many cyclic subgroups
of ﬁnite order.
Proof: When a group G is inﬁnite it has an inﬁnite number of elements; thus it
must certainly contain a countable subset which we enumerate {ai |i ∈ N} ⊆ G,
where ai =aj if and only if i =j.
Each element generates a subgroup Ai = ⟨ai⟩ of G. For each subgroup Ai
we have two options: it is inﬁnite, or it is ﬁnite. If any such subgroup is inﬁnite
then it is isomorphic to Z which has the inﬁnite list of subgroups mZ for each
m ∈ Z; therefore, Ai has an inﬁnite number of subgroups and so so must G.
Not having been forced into this option, consider the alternative that every
Ai is ﬁnite. Once again consider the subgroups ⟨ai⟩. There is no reason to
suspect that each ⟨ai⟩ is distinct; several generators for each could appear in
one group. However, these subgroups are a subset of the lattice of subgroups
of G and therefore they are partially ordered. If there is an inﬁnite chain, or
an inﬁnite number of ﬁnite chains, then there are inﬁnitely many subgroups. 1
Therefore suppose that there are only a ﬁnite number of chains and that each
is ﬁnite length.
This requires that an inﬁnite number of elements be packaged in a ﬁnite
number of subgroups all of which are ﬁnite. A ﬁnite number of ﬁnite sets has
only a ﬁnite number of elements; therefore, this last case cannot be. So G must
have an inﬁnite number of subgroups. □
5 Frattini Subgroup Let G be a ﬁnite group. The Frattini subgroup Φ(G)Hint: Leverage the (proper)
maximality of subgroups to
show two way set contain-
ment.
is the intersection of all maximal subgroups of G. An element g ∈ G is called
a non-generator if whenever ⟨X,g ⟩ =G, we have ⟨X⟩ =G for subsets X ⊆G.
Show that Φ(G) is the set of non-generators of G.
Proof: Suppose an non-generator g is not in the Frattini subgroup. Take any
maximal subgroup M which does not contain g (which exists since g /∈ Φ(G)).
Since M is maximal, it follows:
⟨M,g ⟩ =M ∨ ⟨g⟩ =G.
Since it is assumed to be a non-generator then ⟨M ⟩ =G. Of course this violates
the assumption of M , since M is a maximal proper subgroup. Thus g is in the
Frattini subgroup.
Given any element g ∈ Φ(G), if ⟨X,g ⟩ = G suppose ⟨X⟩ ⁄ = G. What-
ever ⟨X⟩ is, it is contained in a maximal subgroup M then. But this means
⟨X,g ⟩ = ⟨X⟩ ∨ ⟨g⟩ can be no more than M since g and X are both in M .
Thus ⟨X,g ⟩ ⁄ = G. So this last contradiction proves our assertion: the Frattini
subgroup is the group of all non-generators. □
6 Cyclic Automorphisms – True or False? Aut(C8) ∼=C4.Hint: Aut(Zn) = Z×
n .
Example: The assertion is false. We know Aut(C8) = Z×
8 where Z×
8 = {[m] ∈
Z8 | (m, 8) = 1 } under multiplication. Certainly the order of the group is 4, but
it is the Klein 4 group not C4. We see this because
32 = 9 ≡ 1 (mod 8)
52 = 25 ≡ 1 (mod 8)
72 = 49 ≡ 1 (mod 8) .
Thus all the non-trivial elements are of order 2, so no element is of order 4 so
the group cannot be C4. □
1The ﬁrst case can be seen in the Pr¨ ufer group.

Algebra – James Wilson 9
7 Maximal p-subgroups Let G be a ﬁnite group and p be a prime. Show Hint: Recall if N is normal,
then N ∨ H = NH . Also,
the join of normal subgroups is
normal, as is the intersection.
that there exists a normal p-subgroup Op(G) such that H ≤ Op(G) for any
normal p-subgroup H in G. Show that there exists a normal subgroup Op′ (G)
of order prime to p such that H ≤ Op′ (G) for any normal subgroup H in G
whose order is prime to p.
Proof: Consider {Hi | i ∈ I} as the collection of all p-subgroups of G which
are normal in G. Since G is ﬁnite it can only have a ﬁnite number of subgroups
so we can denumerate our Hi’s as H1,...,H n. Since they are normal their join
is simply their complex, that is, that
Op(G) = ⟨H1,...,H n⟩ =H1 · · ·Hn.
We observe this set will be Op(G) since it, by construction, contains all normal
p-subgroups. Since the normal subgroups of a group form a complete modular
lattice, we in fact know the join of these normal subgroups is normal. 2 Moreover,
we use the complex to give us the necessary counting arguments to determine
its order as |H1| · · · |Hn|. Since these are all subgroups of a ﬁnite group their
orders are respectively ﬁnite and so this product is ﬁnite; in fact, they are all
p-subgroups so our resulting group is non-other than a p-subgroup with all the
properties of Op(G).
Now suppose we take K1,...,K m to be all normal subgroups with orders rela-
tively prime to p. Then again using the normal lattice properties we see
Op′ (G) = ⟨K1,...,K m⟩ =K1 · · ·Km,
and once again this is normal; it contains all the Ki’s; and it it has order
|K1| · · · |Km|. Since p does not divide any |Ki| it follows it will not divide their
product; thus, Op′(G) has all the properties we require. □
8 Minimal p-quotients Let G be a ﬁnite group and p be a prime. Show Hint: Recall if N is normal,
then N ∨ H = NH . Also,
the join of normal subgroups is
normal, as is the intersection.
that there exists a normal subgroup Op(G) such that G/Op(G) is a p-group,
andH ≥Op(G), for any normal subgroup H inG such that G/H is a p-group.
Show that there exists a normal subgroup Op′
(G) such that [ G : Op′
(G)] is
prime to p, and H ≤ Op′
(G), for any normal subgroup H in G with [G : H]
prime to p.
Proof: Let {Hi : i ∈ I} be the family of all normal subgroups of G whose
quotient groups arep-groups. As the normal subgroups form a complete lattices,
we may consider the normal subgroup
H =
⋂
i∈I
Hi.
Clearly H ≤Hi for all i ∈I. Now we wish to show [ G :H] = pn for a suitable
n.
Suppose a prime q ⁄=p divides [G :H]. Then there is an element a of order
q in G by Cauchy’s Theorem[ Kle03, Thm-1.5.25]. Thus by the correspondence
theorem [Kle03, Thm-1.4.15], we may pull back a subgroup K which corresponds
to ⟨a⟩ under the projection of G onto G/H. Hence the complex KHi for any
i ∈ I, is a subgroup above both H and Hi. However, [ KHi : Hi] = q which
2We see this also by a direct check:
gH1 · · · Hng−1 = gH1g−1gH2g−1 · · · gHng−1 = H1 · · · Hn.

10 CHAPTER 1. GROUPS
shows that G/Hi is not a p-group. Thus no q other than p divides [G : H] so
H is the group Op(G).
G
pj
KHi
pk
/d127 /d127 /d127 /d127 /d127 /d127 /d127 /d127 /d127 /d127 q
/d63/d63/d63
Hi
pk
/d127 /d127 /d127 /d127 /d127 /d127 /d127 /d127 /d127 /d127
K
q /d63/d63/d63/d63
H
The existence of Op′
(G) is the identical argument, only we assume p does divide
[G :H] and show the impossibility. □
9 Nilpotent Subgroups – True or False? If G is a ﬁnite nilpotent group,Hint: Use the characteriza-
tion of nilpotent groups as
products of Sylow subgroups
together with the fact that the
join of normal subgroups is the
complex.
and m is a positive integer dividing |G|; then there exists a subgroup of G of
order m.
Proof: True, indeed even a normal subgroup of order m can be found. Given
every ﬁnite nilpotent group is a product of its Sylow subgroups, we may write
G ∼=P1 × · · · ×Pn,
where |Pi| = pki
i is the Sylow pi-subgroup for each i. Moreover, for every Pi
there is a chain of normal subgroups in Pi
0 =P 0
i ◁P 1
i ◁ · · · ◁Pki
i =Pi
with |Pj
i | =pj
i .3 Finally we note that if N ◁H thenN × 0 ◁H ×K; thus, each
Pj
i is normal in G in a canonical way. 4
Now we have the tools to construct our desired groups. Take m|n, and
express m in primes:
m =pm1
1 · · ·pmn
n .
As the complex with a normal subgroup is a subgroup we see we may take
H =Pm1
1 Pm2
2 · · ·Pmn
m
to be a subgroup of G, and furthermore we can know the order is simply m.
What is more, as each Pi,j is normal in G we are in the normal subgroup lattice
so we have indeed constructed a normal subgroup of order m in G. □
10 Classiﬁcation of “Local” Groups A non-trivial group G has a properHint: Consider any element in
G\H. subgroup H which contains every proper subgroup of G. What can you say
about G? (Another version: Let G be a ﬁnite group such that for all subgroups
H,K ≤G, we have H ≤K or K ≤H. What can you say about G?)
Example: Indeed the classiﬁcation is that G ∼=Cpi for some prime p and some
i ≥ 1. Since G ⁄=H, G\H is non-empty, so take an element a ∈G\H. Notice
3We know the center of a p-group is non-trivial, and every subgroup of the center is normal,
so we may ﬁnd a normal subgroup of order p. Then we quotient the p group by this subgroup,
repeat the process to ﬁnd a new normal subgroup of order p, use the correspondence theorem
to pull it back to the original and thus construct a chain of p-powered normal subgroups.
4
(a, b)N × 0(a−1, b−1) = aN a−1 × 0 = N × 0.

Algebra – James Wilson 11
⟨a⟩ ≤ G so either G = ⟨a⟩ or ⟨a⟩ ≤ H by the hypothesis on H. Yet a avoidH
so we are forced to conclude that G is cyclic and generated by a.
Now to complete the classiﬁcation we assume G is inﬁnite and immediately
knowG ∼= Z so there are distinct maximal subgroups 2 Z and 3 Z which proveG
does not ﬁt the hypothesis. Thus G must be ﬁnite. But if p,q |n, where n = |G|
then the subgroups ⟨an/p⟩ and ⟨an/q⟩ have indexp andq respectively; thus, once
again we have distinct maximal subgroups. Therefore only one prime divides
the order of G and G is cyclic so G ∼=Cpi.
Indeed the lattice for G is a chain as suggested by the alternate version. □
11 p-subgroup Chains LetG be a ﬁnite group. For each prime p dividing Hint: ShowG is a product of
its Sylow subgroups then in-
voke Exercise-1.10 to conclude
each Sylow subgroup is cyclic.
|G|, letSp(G) denote the set of all p-subgroups ofG. Suppose for each p dividing
|G|, that Sp(G) is totally ordered by inclusion (i.e.: we have H ≤K or K ≤H
for any H,K ∈Sp(G)). Prove that G is cyclic.
Proof: SinceSp(G) is totally ordered and G is ﬁnite, there is a top element in
each chain, and so we take P1,...,P n to be the respective top elements of the
chains of eachpi dividing the order of G. Notice conjugation is an automorphism
so it must send subgroups to subgroups of the same order, but there is a unique
subgroup of maximal pi-th order for each i so we see that each Pi is indeed
normal in G. Moreover, as there orders are relatively prime these groups can
only intersect trivially – precisely stated 5
Pi ∩P1 · · · ˆPi · · ·Pn = 0.
Furthermore from the pigeon-hole principle we know
G =P1 · · ·Pn
so the stage is set to conclude that
G =P1 × · · · ×Pn.
Now we recall one ﬁnal step: in Exercise- 1.10 we saw a ﬁnite group whose lattice
is a chain is simply a cyclic group, so now we may say:
G ∼=Cpi1
1
× · · · ×Cpinn
so G is cyclic by the classiﬁcation of cyclic groups. □
12 Counting Involutions – True or False? If G is a group with even Hint: Partition G into pairs
{a,a −1} then count.number of elements, then the number of elements in G of order 2 is odd.
Proof: The assertion is true. The result falls from the abstraction of a common
notion for groups. Suppose we deﬁne an action of C2 = {1, −1} on a group G
by g ·x = xg where g ∈ C2 and x ∈ G. There are only two issues to check:
1 ·x =x1 =x, and
g(hx) = g(xh) = xhg =xgh = (gh)x.
This natural action makes orbits out of an element and its inverse; thus, each or-
bit has one or two elements; furthermore, orbits of size one correspond precisely
to the trivial element or elements of order 2.
The orbits induced on G are a partition of G so their sizes must sum to G.
When |G| = 2n, the elements of the orbits must add up to 2 n. If we let k be
5The hat means skip this entry.

12 CHAPTER 1. GROUPS
the number of orbits of size two, then we must remove 2 k from 2n to indicate
the number of elements remaining; so there are 2( n −k) elements in orbits of
size one. However, we know the trivial element will always be in an orbit of size
one because it is its own inverse. This leave an odd number, 2( n −k) − 1, of
non-trivial elements, all of which are in orbits of size one and so by construction
are elements of order two. □
13 Nilpotent Extensions Show if N is a normal subgroup of G, and bothHint: S3.
N and G/N are nilpotent, G still may not be nilpotent.
Example: Consider the group S3. The subgroup ⟨(1 2 3) ⟩ is normal in S3
because it has index 2. Since it is also cyclic it is nilpotent. Thus S3/A3 is
nilpotent and A3 is nilpotent. However, S3 is not since the center of S3 is triv-
ial, proving the lower (ascending) central series never begins. 6 □
14 Normal Transitivity – True or False? If X is a normal subgroup of YHint: Consider D8.
and Y is a normal subgroup of Z, then X is a normal subgroup of Z.
Example: The transitivity of normality is generically false. The ﬁrst place we
can test this meaningfully is with the groups of order 8. Naturally we will look
into non-abelian groups where normality is questionable – speciﬁcally D8 since
we know Q8 is Hamiltonian.
For convince, represent D8 in S4 as the group ⟨(1 2 3 4) , (1 3) ⟩. Notice the
subgroup F = ⟨(1 3) ⟩ is of index 2 in the subgroup K4 = ⟨(1 3), (2 4) ⟩ so F is
normal in K4; likewise, K4 is of index 2 in D8 so it is normal in D8. We have
our setup.
The subgroup F is easy to conjugate because it has only one non-trivial
subgroup. Take (1 2 3 4) in D8 and conjugate F :
(1 2 3 4) F (1 4 3 2) = {(1), (2 4) } ⁄=F.
Since F is not invariant under conjugation in D8 it is not normal in D8 and so
we see normality may not be transitive. □
15 Examples of the Parallelogram Law LetG be a ﬁnite group and N ⊴G.Hint: Use the second isomor-
phism theorem. If ( |N |, [G : N ]) = 1, prove that N is the unique subgroup of G having order
|N |.
Proof: SupposeN1 andN2 are normal subgroups of G satisfying the hypothesis
and where |N1| = |N2|. Then their complex is their join. Notice
[N1 :N1 ∩N2]|N1 ∩N2| = |N1| = |N2| = [N2 :N1 ∩N2]|N1 ∩N2|
so j = [N1 : N1 ∩N2] = [N2 : N1 ∩N2] and by the parallelogram law (second
isomorphism theorem would also work), j = [N1N2 : N1] = [ N1N2 : N2]. We
see this in the following diagram.
G
i
N1N2j
/d127 /d127 /d127 j
/d63/d63/d63
N1 j
/d63/d63/d63 N2j
/d127 /d127 /d127
N1 ∩N2
k
0
6Notice this is a special case of a family of such examples: the dihedral groups of orders
not a power of 2.

Algebra – James Wilson 13
[G :N1] = [G :N1N2][N1N2 :N1] = ij and since
|N1| = [N1 :N1 ∩N2]|N1 ∩N2| =jk
we see that we require ( jk,ij ) = 1 to satisfy our assumptions on N1; therefore,
j = 1, so N1 =N2 as [N1 :N1 ∩N2] = 1. □
16 The Complex Subgroup Let G be a ﬁnite group and H,K ≤ G be Hint: Recall any proof of
NH being a subgroup when
N is normal. The normal form
HK =KH replaces the need
for normality.
subgroups. Then HK is a subgroup of G if and only if HK =KH .
Proof: Let H,K be subgroups of G and presume the complex HK is a sub-
group of G. Since HK contains K (1 ∈ H, so 1 ·k ∈ HK for all k ∈ K) it
will be closed to conjugation by K. Given any h ∈ H, k ∈ K, hk ∈ HK by
construction, and therefore k(hk)k−1 =kh ∈HK . So KH ⊆HK , and by the
symmetric argument, HK ⊆KH so in fact HK =KH .
Now suppose HK =KH . Given 1 ∈H and 1 ∈K, 1 · 1 = 1 ∈HK provingHK
is non-empty. Take h,h ′ ∈ H and k,k ′ ∈ K, so that we choose arbitrary ele-
mentshk′,h ′k ∈HK . Since KH =KH there is someh′′ ∈H,k′′ ∈K such that
k′h′ =h′′k′′. With this, the product hk′h′k becomes (hh′′)(k′′k′) which is visi-
bly in HK ; therefore, HK is closed to products. Also, ( hk)−1 =k−1h−1 ∈KH
so in fact ( hk)−1 ∈HK . Therefore HK is a subgroup of G. □
17 Parallelogram Law IfH,K are subgroups of G, then [H :H ∩K] ≤ [G : Hint: Consider the bijection
hH ∩K →hK.K]. If [ G :K] is ﬁnite, then [ H :H ∩K] = [G :K] if and only if G =HK .
Remark 1.0.1 If we allow for a certain abuse of notation we may even say
[H : H ∩K] = [HK : K], where [HK : K] denotes the cosets of K over HK
even if HK is not a subgroup. This reveals the truly combinatorial nature of
the proof.
Proof: Let H/H ∩K and HK/K denote the sets {hH ∩K | h ∈ H} and
{gK |g ∈HK } without any assertions of group structure on H/H ∩K,HK or
HK/K . With this deﬁne a map ϕ :H/H ∩K →HK/K ashH ∩K ↦→hK. The
map is well-deﬁned if wheneverhH ∩K =h′H ∩K it followshK =h′K. But this
is equivalent to asking that h−1h′H ∩K map to K. Since h−1h′H ∩K =H ∩K
it follows h−1h′ ∈ H ∩K so indeed h−1h′ ∈ K; thus, h−1h′K = K so ϕ is
well-deﬁned.
Given h ∈ H such that hK = K it follows h ∈ K and so h ∈ H ∩K so
Ker ϕ ≤ H ∩K. For any h ∈ H ∩K, clearly h ∈ K so hK = K and thus
Ker ϕ=H ∩K. Thus ϕ is injective. For all g ∈HK , g =hk for some h ∈H
and k ∈ K. Thus gK = hkK = hK = ϕ(hH ∩K) so ϕ is surjective and even
now bijective. So we conclude [ H : H ∩K] = [ HK : K] where the abused
notation is understood.
As a corollary we see HK ⊆ G so [H : H ∩K] ≤ [G : K]. Whenever G is
ﬁnite, the pigeon-hole-principle proves [ H : H ∩K] = [ G : K] if and only if
G =HK . □
18 HK -subgroup If H and K are subgroups of ﬁnite index of a group G Hint: Notice [G :K][K :H ∩
K] = [G :H][H :H ∩K].such that [G :H] and [G :K] are relatively prime, then G =HK .
Proof: We let [G :K] = k, [G :H] = h, [H :H ∩K] = i, and [K :H ∩K] = j.
Then we have the following subset lattice (notice the labels on the lines indicate

14 CHAPTER 1. GROUPS
the index of the lesser in the greater):
G
h
/d10 /d10 /d10 /d10 /d10 /d10 /d10 /d10 /d10 /d10 /d10 /d10 /d10 /d10 /d10
k
/d45/d45/d45/d45/d45/d45/d45/d45/d45/d45/d45/d45/d45/d45/d45/d45/d45/d45/d45/d45/d45/d45
m
HK
j/d119 /d119 /d119 /d119 /d119 /d119 /d119 /d119 /d119
i
/d52/d52/d52/d52/d52/d52/d52/d52/d52/d52/d52/d52/d52/d52/d52
H
i
/d52/d52/d52/d52/d52/d52/d52/d52/d52/d52/d52/d52/d52/d52/d52
K
j
/d119 /d119 /d119 /d119 /d119 /d119 /d119 /d119 /d119
H ∩K
H ∩K is a subgroup in G. Furthermore both [ G : H] and [ G : K] are
ﬁnite indices, so by the Lemma of Poincar´ e ([ Hun74, Proposition-I.4.9]) we
know [G :H ∩K] ≤ [G :H][G :K] and is therefore ﬁnite. From the Theorem
of Lagrange ([ Hun74, Theorem-I.4.5]) we know: [ G : H][H : H ∩K] = [ G :
H ∩K] = [G :K][K :H ∩K], which are all ﬁnite products.
We must resolve when hi =kj knowing (h,k ) = 1. Since h and k are rela-
tively prime it follows h|j andk|i, so h ≤j andk ≤i. But by Proposition-I.4.8
we see j = [K :H ∩K] ≤ [G :H] = h and likewise i ≤k. Therefore i =k and
j = h. Finally Proposition-I.4.8 concludes since [ H : H ∩K] = [ G : K] then
G =HK . □
19 Hamiltonian Groups – True or False? All subgroups of Q8 are normal.Hint: The maximal subgroups
have index 2 and intersections
of normal subgroups are nor-
mal.
Example: This is true as Q8 is a Hamiltonian group. To see this notice the
elementsi,j,k all determine distinct subgroups of order 4 – which means they
have index 2, so they are normal. These maximal subgroups intersect at ⟨−1⟩
and since the normal subgroups form a lattice, this intersection is normal. The
only subgroups remaining are the entire group and the trivial group both of
which are trivially normal. Thus all subgroups are normal.
That these are indeed all the subgroups follows from the observation that
the only element of order 2 is -1, so there can be no C2 ×C2 subgroups, and all
the cyclic order 4 subgroups are accounted for. □
20 Center of Sn The center of Sn is trivial for n ≥ 3.Hint: Conjugate using cycles
and the fact that conjugation
permutes indices.
Example: Let n >2 and consider the center of Sn. Since disjoint cycles are
independent of each other we may test for centrality on just the elements in the
cycle. Given a central element σ, pick a cycle κ = (a1,...,a i), with 2 < i≤n
out of σ which consequently must also be central.
Next take τ to be τ = (a1,a 2). Now conjugate:
κτκ −1 = (a1,...,a i)(a1a2)(ai,...,a 1) = (a2a3) ⁄=τ.
Therefore κ is not central forcing σ to be the same.
This leaves us only the case where σ is a product of disjoint transpositions.
Now consider a cycle in such an element: it must take the from κ = (a1,a 3).
But since n> 2 we know there exists a τ = (a1,a 2,a 3) and we simply conjugate:
κτκ −1 = (a1,a 3,a 2) = τ −1 ⁄=τ.

Algebra – James Wilson 15
So once again neither κ norσ are central, so indeed the center of Sn is trivial. □
21 Parallelogram Example IfN ⊴G, |N | is ﬁnite, H ≤G, [G :H] is ﬁnite, Hint: Draw a parallelogram
then justify the index of the
desired side is 1.
and [G :H] and |N | are relatively prime, then N ≤H.
Proof: We know [G :H] is ﬁnite so [ NH :H] is ﬁnite and as always it follows
[NH :H] = [H :N ∩H]. Also |N | is ﬁnite so from the theorem of Lagrange we
know
|N | = [N :H ∩N ]|H ∩N | = [NH :H]|H ∩N |
(where all the pieces here are ﬁnite) and [ G : H] = [ G : NH ][NH : H]; thus,
since these two numbers are relatively prime, it follows [ NH :H] = 1 so N ≤H.
□
22 Q subgroups (Q, +) does not have subgroups of ﬁnite index. Hint: Use the index of the
subgroup to annihilate any el-
ement in the quotient group.
Proof: Given any subgroup H of Q we know H is normal in Q as Q is abelian.
Let n = [ Q : H]. By the theorem of Lagrange every element in Q/H as order
dividing n. So carelessly take any coset a
b +H and write
a
b +H = na
nb +H =n
( a
nb +H
)
= 0.
Thus Q/H is trivial so n = 1 and thus all proper subgroups of Q have inﬁnite
index. □
23 Finite Index Intersections If H and K are ﬁnite index subgroups in G, Hint: Use the Parallelogram
Law (Exercise- 1.17).then so is H ∩K.
Proof: Recall from the Parallelogram Law that [ H : H ∩K] ≤ [G : K]. Yet
[G :K] is ﬁnite so [ H :H ∩K] must also be ﬁnite. Now we use the Lagrange’s
Theorem to see
[G :H ∩K] = [G :H][H :H ∩K]
which is a product of ﬁnite numbers so it is ﬁnite. □
24 Unions of Conjugation IfH is a proper subgroup of ﬁnite a ﬁnite group Hint: Make an estimation of
the order of the union from the
index of the normalizer.
G, then the union ⋃
g∈GgHg −1 is not the whole G. [See also Exercise- 1.25.]
Proof: The number of subgroups conjugate to H is given by the index of the
normalizer NG(H) in G. As H ⁄=G it follows if H is normal it conjugacy class
contains only itself so G is not the union of the conjugate subgroups of H. So we
therefore know H is strictly contained in NG(H) so indeed 1 < [G :NG(H)]<
[G :H]. Now let n denote the cardinality of ⋃
g∈GgHg −1. As the identity is in
common with each gHg −1, and possibly more, we may bound n as follows:
n ≤ [G :NG(H)](|H| − 1) + 1 ≤ [G :H](|H| − 1) + 1 = [G :H]|H| − [G :H] + 1.
Using the theorem of Lagrange we see this is simply:
n ≤ |G| − [G :H] + 1< |G|,
the last step justiﬁed as [ G : H] > 1. Thus the cardinalities do not agree so
that G is not the proposed union. □

16 CHAPTER 1. GROUPS
25 Unions of Conjugation If H <G and of ﬁnite index, then G is not theHint: Mimic Exercise-1.24 us-
ing G/⋂
g∈GgHg −1 as a set
(not as a group) instead.
union⋃
g∈GgHg −1.
Proof: The number of subgroups conjugate to H is given by the index of the
normalizer NG(H) in G. As H ⁄=G it follows if H is normal it conjugacy class
contains only itself so G is not the union of the conjugate subgroups of H. So we
therefore know H is strictly contained in NG(H) so indeed 1 < [G :NG(H)]<
[G :H]< ∞.
We also pause to provide a technical result: [ G :H] = [G :gHg −1] for any
group G and subgroup H and element g ∈G. To see this take a transversal T
of G/H – as a set only (that is a subset of G for which h,k ∈ T , hH = kH
implies h =k and G/H = {kH : k ∈T }). This is because
⋃
k∈T
kH =G =gGg −1 =
⋃
k∈T
gkHg −1 =
⋃
k∈T
gkg −1gHg −1 =G/gHg −1.
So we see the natural bijection of transversal so the indices are equal. Thus
both are also ﬁnite as one is.
Now take K = ⋂
g∈GgHg −1. As there are only ﬁnitely many subgroups
conjugate to H, by induction and Exercise- 1.23 we have that the intersection of
ﬁnitely many subgroups of ﬁnite index is of ﬁnite index as well.
TreatingH/K as the set {hK : h ∈ H} we let n denote the cardinality
of⋃
g∈Gg(H/K)g−1. As the identity is in common with each g(H/K)g−1, and
possibly more, we may bound n as follows:
n ≤ [G :NG(H)]([H :K] − 1) + 1 ≤ [G :H]([H :K] − 1) + 1
= [ G :H][H :K] − [G :H] + 1 = [G :K] − [G :H] + 1< [G :K],
the last step justiﬁed as [ G : H] > 1. Hence the conjugate subgroups do not
cover the elements in the quotient (as a set only) so they will not cover the
elements in the inter group G. □
26 Conjugacy Classes and Generators Let G be a ﬁnite group G, andHint: Use Exercise- 1.25 to
show that the subgroup gener-
ated by these elements cannot
be proper.
g1,...,g l be representatives of the conjugacy classes of G; thenG = ⟨g1,...,g l⟩.
Proof: Let H = ⟨g1,...,g l⟩. We must show H is not a proper subgroup
of G. Since we have a representative from each conjugacy class it follows
G = ⋃
g∈GgHg −1. However form Exercise- 1.25 we know this cannot occur
(note since all is ﬁnite certainly [ G :H] is ﬁnite) so H must be G itself. □
27 GLn(Fq) The group GLn(Fq) has an element of order qn − 1.Hint:
Proof: Consider Fqn as a Fq vector space. It is clear that the dimension is n
so as an abelian group it splits as
Fqn ∼= Fn
q.
NowGLn(Fq) is precisely the group of all linear automorphisms of Fn
q ; therefore,
also of Fqn in a natural way. However we know that set of linear automorphisms
of Fqn contains F×
qn and furthermore that any ﬁnite subgroup of the multiplica-
tion of a ﬁeld is cyclic – so indeed
F×
qn ∼=Cqn−1.
ThusGLn(Fq) contains a copy of Cqn−1. So indeed there is an element of order

Algebra – James Wilson 17
qn − 1 in GLn(Fq). 7 □
28 Conjugate Cluster Let H be a subgroup of a group G. Let Hint: For closure show H ∩
ghHh −1g−1 contains H ∩
gHg −1 ∩hHh −1.C := {g ∈G | H ∩gHg −1 has ﬁnite index in both H and gHg −1}.
Show that C is a subgroup of G.
Proof: Notice of course H ∩ 1H1 = H so 1 ∈C provingC is non-empty.
Next take g,h ∈C. From Exercise- 1.23 we know
[H :H ∩gHg −1 ∩hHh −1]
is ﬁnite as [ H : H ∩gHg −1] and [ H : hHh −1] are both ﬁnite. Now we need
only show that H ∩ghHh −1g−1 containsH ∩gHg −1 ∩hHh −1 and we will have
shown that [H :H ∩ghHh −1g−1] is ﬁnite since then
[H :H ∩ghHh −1g−1] ≤ [H :H ∩gHg −1 ∩hHh −1].
Moreover, mutatis mutandis, we will have [ghHh −1g−1 :H ∩ghHh −1g−1] ﬁnite
as well so we will be able to conclude that gh ∈C.
Well certainly if u ∈ H ∩gHg −1 ∩hHh −1 then huh−1 ∈ H which means
ghuh−1g−1 ∈H so indeed anyu in this given intersection also lies inghHh −1g−1.
So we have our desired set containment.
Finally take g ∈C. We know [ H :H ∩gHg −1] is ﬁnite as is [ gHg −1 :H ∩
gHg −1]. Now simply conjugate by g−1. Since conjugation is an automorphism
the indices must be preserved; thus,
[gHg −1 :H ∩gHg −1] = [g−1gHg −1g :g−1(H ∩gHg −1)g] = [H :g−1Hg ∩H]
is ﬁnite and
[H :H ∩gHg −1] = [g−1Hg :g−1(H ∩gHg −1)g] = [g−1Hg :g−1Hg ∩H]
is as well, so g−1 ∈C. □
29 3 Sylow-2-subgroups Suppose that a ﬁnite group G has exactly three Hint: Act on the Sylow sub-
groups by conjugation and
show that the kernel of the ac-
tion cannot contain all three
Sylow-2-subgroups.
Sylow 2-subgroups. Show that every permutation of these Sylow subgroups can
be obtained by conjugation by some suitable element in G.
Proof: Let G act on the Sylow-2-subgroups by conjugation. It follows this
action is closed as Sylow-2-subgroups can only be conjugate to other Sylow-2-
subgroups in a ﬁnite group. Moreover the action is transitive so the induced
homomorphismf :G →S3 must coverA3. That is to say that [ G :Ker f] ≥ 3.
So we have only two choices: [ G :Ker f] = 3 or [ G :Ker f] = 6 in which case
f is surjective. If f is surjective then we have conﬁrmed that every permutation
of the Sylow-2-subgroups can be had by appropriate conjugating elements.
Now suppose instead that [ G : Ker f] = 3. As G as distinct Sylow-2-
subgroups it must therefore have non-trivial Sylow-2-subgroups so indeed 2 di-
vides the order of G. Moreover now we see that as [ G : Ker f] = 3, every
7The element in question can be determined as
A =


1 · · · 1
1 0
... . . . . . . ...
1
1 0 · · · 0



18 CHAPTER 1. GROUPS
Sylow-2-subgroup must be contained inside Kerf or otherwise the index would
be even by the correspondence theorem. However we may also characterize the
kernel as the intersection of all the normalizers. If we take S1,S 2 and S3 to be
the Sylow-2-subgroups, then S1,S 2,S 3 ≤Ker f ≤NG(S1) so it follows that S1
is not conjugate to S2 orS3 insideNG(S1). However, S1 is a Sylow-2-subgroup
of NG(S1) so it must be conjugate to all other Sylow-2-subgroups in NG(S1)
which contradicts the previous result. Therefore Ker f cannot contain all the
Sylow-2-subgroups so indeed [ G :Ker f] = 6. □
30 Inﬁnite Simple Groups Prove that any inﬁnite simple group G has noHint: Consider that left regu-
lar action on a ﬁnite index sub-
group.
subgroup of ﬁnite index.
Proof: SupposeG is an inﬁnite simple group with a subgroup H of ﬁnite index
n. Certainly G acts transitively on the left cosets of H so there is an induced
homomorphism f : G → Sn. Since G is simple, the kernel of f may only be
trivial or G. A trivial kernel requires the impossibility of embedding an inﬁnite
number of elements in a ﬁnite group. Making G the kernel forces the action of
the left cosets to be trivial, not transitive. With no options left, we conclude H
was a fantasy to begin with. □
31 Simple Groups of order 120 Prove that there is no simple group ofHint: Consider Sylow-5-
subgroups and show G is then
impossibly embedded in A6.
order 120.
Proof: From the third Sylow theorem it follows there are either 1 or 6 Sylow-5-
subgroups. If G is to be simple then there must be 6. Thus conjugation induces
a homomorphism f : G → S6. Moreover, the kernel must be trivial if G is
simple, thus f is and embedding. If G is not completely contained in A6 then
G ∩A6 is a normal subgroup of G. Thus G ≤ A6. However this cannot be as
[A6 : G] = 6! /(2 · 120) = 3 and we know to keep A6 simple there can be no
subgroup of index 2 ,..., 5.
So while it is possible to have a 6 Sylow-5-subgroups – for example S5 – it
is not possible to avoid a normal subgroup somewhere in G. □
32 Simple Groups of order 2472 The groups of order 2 4 · 72 are not simple.Hint: Count the Sylow sub-
groups. Example: The number of Sylow 7-subgroups r7 must divide 2 4 · 72 and be
congruent to 1 modulo 7. The possible choices are 1,2,4,8, and 16. Of these
only 1 is congruent to 1 mod 7. Therefore there is one Sylow 7-subgroup.
Since conjugation is an automorphism, a lone Sylow 7-subgroup must be
invariant to conjugation and thus it must be normal. Therefore all groups of
this order are non-simple. □
33 Simple Groups of order 150 Prove that there is no simple group ofHint: Notice 52 ∤ (6 − 1)!
order 150.
Proof: Using [ Kle03, Thm-1.7.13] we know a group of order 150 = 2 · 3 · 52 is
not simple as (5 , 6) = 1 yet 5 2 ∤ 5!. □
34 Simple Groups of order 80. Show that a group of order 80 must haveHint: Consider conjugation
on Sylow-2-subgroups. a non-trivial normal subgroup of order a power of 2.
Example: By the third Sylow theorem we knew a group G of order 80 has either
1 or 5 Sylow-2-subgroups. If it is 1, then G has a proper normal subgroup of
order a power of 2, as requested. So presume that now there are 5 Sylow-2-
subgroups.

Algebra – James Wilson 19
As Sylow-2-subgroups are conjugate we have an induced homomorphism f :
G → S5 which represents the action of conjugation on the Sylow-2-subgroups.
As 80 does not divide 120, we are forced to acknowledge there is a non-trivial
kernel for f . Moreover, if g any element in G, then if gHg −1 = H for every
Sylow-2-subgroupH, then g ∈NG(H) for each H. However, the index of every
Sylow-2-subgroup in G is prime, 5, so NG(H) = H or else H would be normal
in G. Hence we see that the kernel of f lies inside the Sylow-2-subgroups of G
and so there is a non-trivial proper normal 2-subgroup of G. □
35 D8 Representation Prove that the group of upperunitriangular 3 × 3 Hint: Use v. Dyck’s theorem.
matrices over F2 is isomorphic to D8.
Proof: Let U3(F2) be upperunitriangular matrices and deﬁne the map f :
D8 →U3(F2) on the generators as follows:
f (a) =


1 1 1
0 1 1
0 0 1

 ; f (b) =


1 1 0
0 1 0
0 0 1

.
It is easy to verify f (b)2 =I3 and
f (a)2 =


1 0 1
0 1 0
0 0 1

 ; f (a)4 =I3.
Now
f (b)f (a)f (b)−1 =


1 1 0
0 1 0
0 0 1




1 1 1
0 1 1
0 0 1




1 1 0
0 1 0
0 0 1

 =


1 1 0
0 1 1
0 0 1

 =f (a)−1.
Now that we have satisﬁed all the relations we use v. Dyck’s Theorem to
conclude f extends to a homomorphism from D8 to U3(F2). Moreover, the
kernel of f is trivial as the order of f (a) and a and f (b) and b agree. Finally,
|U3(F2)| = 2 3 = 8 so by the pigeon-hole principle f is surjective so f is an
isomorphism. □
36 Trivial Relations Let G be a ﬁnite group with g ∼ g2 for every g ∈ G. Hint:
Prove that G = 1.
Remark 1.0.2 The following proof is an exercise in killing a ﬂee with an
atomic bomb; it should not be viewed as the best proof.
Proof: Let a ∈ G and take g ∈ G so that a2 = gag −1. Since conjugation is
an isomorphism, it follows the order of a2 is that of a. Thus the order of a is
odd. Moreover since every element has odd order, the order of the group must
be odd so it must be solvable.
Now notice
[g,a ] = gag −1a−1 =a2a−1 =a
so G =G′. Since G is solvable, but has as a derived series that does not start,
it follows G is the trivial group. □
37 2 Conjugacy Classes Suppose that a ﬁnite group G has exactly two Hint: The order of each con-
jugacy class must divide the
order of the group.
conjugacy classes. Determine G up to isomorphism.

20 CHAPTER 1. GROUPS
Proof: One conjugacy class must always be that of the trivial element, and it
contains exactly this one element. By our assumption all other elements of G
are in the second conjugacy class. If G has order n then we are saying there is
a conjugacy class of order n − 1. However since this is an orbit, it must divide
the order of G so in fact n − 1|n. Since ( n − 1,n ) = 1 the only case this can
occur is when n = 2. Thus G ∼=C2. □
38S4 – True or False? S4/V4 ∼=S3.Hint: LetS4 act on its Sylow-
2-subgroups. Proof: This is true. We know the number of Sylow-2-subgroups is 1 or 3 by
the third Sylow theorem. Easily we see there are 6 elements of the form ( a,b ),
and three of the from ( a,b )(c,d ). All these having order 2 must be contained in
some Sylow-2-subgroup, but there are 9 and the order of the Sylow-2-subgroups
is 8, so there must be 3 Sylow-2-subgroups, not 1.
From Exercise-1.29 we know that S4’s action on the Sylow-2-subgroups by
conjugation yields a surjection onto S3. Thus we have f :S4 →S3 and all we
need to identify is the kernel so we may conclude that S4/V4 ∼=S3 by the ﬁrst
isomorphism theorem.
In particular, the subgroups of order 4 are cyclic or C2 ×C2. In the ﬁrst case
⟨(1234)⟩ is conjugate to ⟨(1324)⟩ via (23) so they cannot be normal. Likewise
⟨(12), (34)⟩ and ⟨(13), (24)⟩ are conjugate via (23) again. So the only order 4
subgroup that is normal in S4 is V4. Thus it must be the kernel. □
39 Transitive Subgroups ofS5 – True or False? Every subgroup of orderHint: Every element of order
5 is of the form (a1,...,a 5). 5 of S5 is transitive.
Proof: This is true. A subgroup of order 5 must be a cyclic subgroups and
thus corresponds entirely to elements of order 5 in S5. When we write an el-
ement as a product of disjoint cycles α = α1 · · ·αn we immediately know its
order to be the least common multiple of the length of each cycle αi. Since 5 is
prime it follows the only permutations that can be of order 5 are those which
are a product of disjoint length 5 cycles. However we only have 5 elements to
act on so each element of order 5 in S5 takes the form α = (a1,...,a 5) with
{a1,...,a 5} = {1,..., 5}. Without loss of generality let a1 = 1 – we can rotate
the permutation until this is so – and choose any point b = 1,..., 5. It follows
b =ai for some i = 1,..., 5 so indeed αi(1) = b so the orbit of 1 is {1,..., 5} so
the group ⟨α⟩ acts transitively. As this is an arbitrary order 5 subgroup of S5
we know all subgroups of order 5 in S5 are transitive. □
40pq-groups – True or False? Ifp andq are primes, then a group of orderHint: Any (the) non-abelian
group of order pq will serve. pq is nilpotent.
Example: As with Exercise-13, the group S3 serves as an example. The order
ofS3 ispq wherep = 2,q = 3 but it is not nilpotent because its center is trivial;
thus its upper ascending central series never begins.
Moreover, whenever q ≡ 1 (mod p), the non-abelian group of order pq is
never nilpotent for the same reason. □
41 Metabelian A group G is call metabelian of there exists a normal sub-Hint: Use the isomorphism
theorems. group N of G with N and G/N both abelian. Prove that every subgroup of
a metabelian group is metabelian. Prove that every quotient of a metabelian
group is metabelian.
Proof: Let H ≤G. Certainly N ∩H ⊴H as N ⊴G. Moreover, N is abelian
so so must be all its subgroups, including N ∩H. By the second isomorphism

Algebra – James Wilson 21
theorem we know NH/N ∼=H/N ∩H, and as G/N is abelian, and NH/N is a
subgroup of G/N, it follows NH/N is abelian; therefore, H/N ∩H is abelian.
Hence H is metabelian.
Let K ⊴G and consider G/K. As both N and K are normal it follows
NK is normal so NK/K is normal in G. Moreover, NK/K ∼= N/N ∩ K
which we know to be abelian because it is the quotient of an abelian group
– namely of N . Thus G/K as a normal subgroup NK/K which is abelian.
Finally, (G/K)/(NK/K ) ∼= G/NK by the third isomorphism theorem. Yet
N ≤NK andG/N is abelian, so G/NK is abelian proving that indeed G/K is
metabelian. □
42 Normalizers of Sylow subgroups – True or False? If P is a Sylow p- Hint: Sylow p-subgroups are
conjugate.subgroup of the ﬁnite group G, then NG(P ) contains just one Sylow p-subgroup
of G.
Proof: IfP is a Sylowp-subgroup ofG, then it must also be a Sylow p-subgroup
of NG(P ). However it is also normal in NG(P ) so it may not be conjugate to
any other subgroup of NG(P ). If there is another Sylow p-subgroupQ, of G, in
NG(P ) then it would also be a Sylow p-subgroup of NG(P ) and thus it would
be conjugate to P . As just stated this cannot occur so NG(P ) may not contain
any other Sylow p-subgroup but P itself. □
43 Inherited Sylow subgroups If H ≤G are ﬁnite groups, then rp(H) ≤ Hint: Use normalizers.
rp(G).
Proof: First notice we may describe the number of Sylow p-subgroups by the
the counting arguments of group actions: all Sylow p-subgroups are conjugate,
so rp(G) = [G :NG(P )] for any Sylow p-subgroup P . Every Sylow p-subgroup
PH of H is a p group of G so it can be extended to a Sylow p-subgroup PG in
G. Thus PH =PG ∩H. In the same way NG(PG) ∩H =NG(H). Therefore
rp(G) = [G :NG(PG)] ≥ [H :NH (PG ∩H) = [H :NH (PH )] = rp(H)
by the parallelogram law. □
44 Normalizers of Sylow-subgroups. Let H ≤G be ﬁnite groups, P be Hint:
a Sylow-p-subgroup of H, and NG(P ) ≤H. Then P is a Sylow-p-subgroup of
G.
Proof: Suppose Q is a Sylow-p-subgroup of G containingP . Take any g ∈P .
ClearlygPg −1 =P and asP ≤Q alsogQg −1 =Q so indeedg ∈NG(P )∩NG(Q)
so that P ≤NG(P ) ∩NG(Q).PENDING: I don’t know. □
45 Simple Groups of Order pqr. If |G| =pqr, show that G is not simple, Hint: Count the number of el-
ements required to avoid nor-
mal Sylow subgroups.
with p,q and r prime.
Proof: Suppose p<q <r . Then we know the total number of elements in G
must be bounded below by
1 +rp(p − 1) +rq(q − 1) +rr(r − 1).
From the Sylow theorems we know rr = 1,pq , and we focus on rr =pq since we
suspect G is simple. Also rq = 1,r,pr , the best case is that rq ≥r. Finally for
the same reasons rp ≥q as we want only a lower bound. This gives us:
1 +q(p − 1) +r(q − 1) +pq(r − 1) = pqr + (qr + 1) − (q +r).

22 CHAPTER 1. GROUPS
Howeverq +r < qr+ 1 and so our total number exceeds the allocation of pqr
many elements. So we recognize one of the Sylow subgroups is unique and thus
normal; hence, G is not simple. □
46 Simple Groups of Order p(p + 1). Let |G| = p(p + 1), where p isHint: In the case where there
is no normal p-subgroup, con-
sider P = ⟨g⟩ and show that
gixP ⁄=gjxP for any x /∈P .
Then use this to show the non-
p-elements all take the form
gixg−i.
prime. Show G has either a normal subgroup of order p or a normal subgroup
of order p + 1. 8
Proof: Consider the Sylow- p-subgroups. If rp = 1, then there is a normal
Sylow-p-subgroup.
Now suppose instead that rp = p + 1, and let P be a Sylow- p-subgroup.
GivenP is of prime order it is cyclic so there exists a generator g ∈P . No take
an element x ∈G which is not in any of the Sylow- p-subgroups. It is clear that
x does not have order p.
Now we study the cosets (without making assumptions that P is normal.)
If gixP =gjxP , then gi−jxP =xP and even x−1gi−jx ∈P . If i ⁄=j then gi−j
generates P so indeed x−1Px = P . Notice, furthermore, that [ G : NG(P )] =
p + 1 since rp =p + 1, so indeed NG(P ) = P . However, gi−j ∈P and x is not,
so x−1Px ⁄=P . This means that i =j. Therefore the cosets
P, xP, gxP, · · ·, g p−1xP
are all distinct. Furthermore, as there are p + 1 of them, they are all the cosets
of P . This means the following representatives from each coset are distinct:
1, x, gxg −1, · · ·, g p−1xg−(p−1).
More to the point, as x is not of order p, neither is gxg −1, throughgp−1xg−(p−1),
and none are trivial. Of the total p(p + 1) elements, 1 + (p − 1)(p + 1) of them
are found in Sylow-p-subgroups leaving only p many non-p-elements. These are
precisely the gixg−i elements, and each is found in one and only one coset of P .
Now we can conclude that the non- p-elements are closed under multiplica-
tion. Take x and y to be two non-trivial, non- p-elements. If xy is contained in
a Sylow-p-subgroup, then without loss of generality we may assume xy ∈P . So
y ∈x−1P . Yet x−1 ∈P , and certainly x−1 is a non-p-element. As every coset
has a unique non- p-element it follows y =x−1 so xy lies in a Sylow- p-subgroup
if and only if xy = 1. So multiplication of non- p-elements is closed.
As such that set H of all non-p-elements is the lone subgroup of order p + 1
so it is trivially normal. 9 □
47 Cyclic Sylow-2-subgroups. Let a ﬁnite group G have a cyclicHint: Consider the Cayley
representation of G and its in-
tersection with An.
Sylow-2-subgroup. Show that G has a subgroup of index 2.
Proof: Let n = |G|. We choose ﬁrst to represent G as a permutation group
under the traditional Cayley representation of left regular action. Notice then
that G ∩An is a subgroup of G which has at most index 2 – as we know
[G :G ∩An] ≤ [Sn :An] = 2.
So if we can demonstrate that G ⁄=An then we will be forced to conclude that
G ∩An has index 2 in G.
8This is a trivial result if it is observed that G is a Frobenius group. However, the proof that
Frobenius groups are semi-direct products requires character theory and is therefore outside
the nature of this chapter.
9Note that moreover every non-trivial element of H is conjugate, so indeed, H ∼= Cq ×
· · · × Cq for some prime q and in fact this occurs if and only if p + 1 = qi for some prime q.

Algebra – James Wilson 23
As n = |G| we take n = 2km with (2,m ) = 1. We are given that G has a
cyclic Sylow-2-subgroup, so we may say it is generated by an element g of order
2k. Hence under the regular representation we ﬁnd g is represented by
(h1,gh 1,g 2h1,...,g 2k−1h1) · · ·(hm,ghm,g 2hm,...,g 2k−1hm)
where the hi’s are a transversal for the cosets of ⟨g⟩. Each of these cycles has
even length so it follows as permutations they are odd permutations, and as m
is also odd, the total sign of our permutation representation of g is odd times
odd which is odd. Hence G contains an odd element, namely the regular repre-
sentation of g, and as such it follows G ⁄=An. □
48 Automorphism of Sn. Let n ⁄= 6. Then every automorphism of Sn is Hint:
inner.
Proof: Let f : Sn → Sn be an automorphism of Sn, for n ⁄= 6. We know f
must send conjugate subgroups to conjugate subgroups as
f (gHg −1) = f (g)f (H)f (g)−1.
We know that the stabilizers of points, 1 ,...,n , are all conjugate as they are
stabilizers of the same action – namely Sn acting on 1,...,n . Denote StabSn(k)
bySk
n−1 and notice they are isomorphic to Sn−1 for eachk = 1,...,n . It follows
any automorphism of Sn is therefore a permutation on the Sk
n−1 subgroups. □
49 Automorphism of S6. The group S6 has an automorphism mapping Hint:
the stabilizer of a point in S6 to a transitive subgroup. No such automorphism
can be inner.
Example:
□
50 Nilpotency and Normalizers. Let G be a ﬁnite group. Then G is Hint: The normalizer of a
product is the product of the
normalizers.
nilpotent if and only if H is a proper subgroup of NG(H), whenever H is a
proper subgroup of G.
Proof: Suppose G is nilpotent, then it is is the direct product of it Sylow
p-subgroups; say G =P1 × · · · ×Pn. Now take H a proper subgroup of G. Since
there is a unique Sylow p-subgroup for each p dividing the order of G, it follows
H =H ∩P1 × · · · ×H ∩Pn. Now it follows
NG(H) = NG(H ∩P1) × · · · ×NG(N ∩Pn).
If each NG(H ∩Pi) = H ∩Pi then H =G because the normalizer of a proper
subgroup of any Sylow p-subgroup will be at least P and when G is nilpotent
G. Thus H is strictly contained in NG(H).
In the converse take any Sylow p-subgroup Pi. Then if G = Pi it is nilpo-
tent. If not then Pi is proper so NG(Pi) ⁄= Pi. However we know for Sylow
p-subgroups that NG(NG(Pi)) = NG(Pi) so the only case this can occur is
when NG(Pi) = G. Therefore each Sylow subgroup is normal in G so G is
nilpotent. □
51 Dihedral Nilpotency. – True or False? D2n is nilpotent. Hint: Note that
D4n/Z(D4n) ∼=D2n.
Lemma 1.0.3 D2in/⟨ai⟩ ∼=D2n.

24 CHAPTER 1. GROUPS
Proof: Since ⟨a⟩ is a cyclic normal subgroup, all its subgroups are normal.
Therefore ⟨ai⟩ is normal. Notice, ⟨ai⟩ has index n in ⟨a⟩; therefore, a⟨ai⟩ has
order n. Likewise, b⟨ai⟩ has order 2. Since ⟨ai⟩ has index 2n in D2n, it follows
D2in/⟨ai⟩ has order 2n. Finally,
b⟨ai⟩a⟨ai⟩ =ba⟨ai⟩ =a−1b⟨ai⟩ =a−1⟨ai⟩b⟨ai⟩.
Therefore D2in/⟨ai⟩ ∼= D2n since it has the same presentation of the dihedral
group D2n. □
Theorem 1.0.4 D2n is nilpotent if and only if n = 2k for some k.
Proof: If n = 1 = 2 0 then D2n is C2 which is nilpotent; likewise when n = 2,
D2n is abelian so it is nilpotent. Now consider n> 2.
From Exercise-1.77 we know the center of D2n is trivial if and only if n is
odd. So if n has any odd factors we use the above lemma to quotient out the
centers and arrive at D2m where (2,m ) = 1. Here the center is ﬁnally trivial
so the ascending central series does not terminate with the whole group so it is
not nilpotent. Whenever n has no odd factors it is a 2-group so it is nilpotent. □
52 Sylow-subgroups of Quotients. Let ϕ : G → H be a surjectiveHint: Use the ﬁrst isomor-
phism theorem. homomorphism of ﬁnite groups. If P is a Sylow- p-subgroup of G, then ϕ(P )
is a Sylow- p-subgroup of H. Conversely, every Sylow- p-subgroup of H is the
image of a certain Sylow- p-subgroup of G.
Proof: TakeK = Ker ϕ. Let |P | = pn. By the parallelogram law we know
[PK : K] = [ P : P ∩K] = pi. Hence PK/K is a p-subgroup of G/K. Also,
i = [G/K :PK/K ] = [G :PK ] but as P is a Sylow-p-subgroup in G, it follows
(i,p ) = 1. Thus, PK/K is indeed a Sylow- p-subgroup of G/K. By the ﬁrst
isomorphism theorem we see in fact ϕ(P ) is a Sylow- p-subgroup of H.
Now take Q a Sylow-p-subgroup of H. It follows K ≤ ϕ−1(Q). Now take
P to be a Sylow- p-subgroup of ϕ−1(Q). If P is not a Sylow- p-subgroup of G,
then there exists some Sylow-p-subgroupP ′ containingP . Such a subgroup also
contains K, and so pj = [P ′ : K] > [P : K] = pi with i < j. However, this
produces a strictly large p-subgroup in the quotient space G/K. This applies to
H by the ﬁrst isomorphism theorem so indeed such a P ′ cannot exist. Therefore
P is a Sylow-p-subgroup of G and ϕ(P ) = Q. □
53 Sylow-subgroups of Normal subgroups. Let G be a ﬁnite group,Hint: Use conjugation of
Sylow-p-subgroups prove P ∩
N is Sylow in N .
N ⊴G, and P a Sylow-p-subgroup of G for some prime p. Show that PN/N is
a Sylow-p-subgroup of G/N and P ∩N is a Sylow-p-subgroup of N .
Proof: Takeϕ : G → G/N to be the canonical projection. Now make use of
Exercise-1.52 to conclude that PN/N is Sylow-p-subgroup of G/N. That P ∩N
is a Sylow-p-subgroup of N follows with a little more care.
SupposeQ is a Sylow-p-subgroup ofN containingP ∩N . Then Q is contained
in some Sylow- p-subgroup of G, call it P ′. Thus P and P ′ are conjugate, say
byg. Hence:
gP ∩Ng −1 =gPg −1g ∩Ng −1 =P ′ ∩N =Q.
Thus |Q| = |P ∩N | which means Q = P ∩N so indeed P ∩N is a Sylow- p-
subgroup of N . □
54 Conjugacy Classes. If a group G contains an element having exactlyHint: Act on the order conju-
gacy class.

Algebra – James Wilson 25
two conjugates, then G has a non-trivial proper normal subgroup.
Proof: Let X = {a,b } be the given conjugacy class of order 2. Note that G
acts transitively on X by conjugation. This induces a natural surjection G →S2
proving G has a normal kernel of index 2. Thus G =C2, or the subgroup is a
proper non-trivial normal subgroup. If G =C2 then there is no conjugacy class
of order 2. □
55 Embedding in An. Any ﬁnite group is isomorphic to a subgroup of An Hint: Attach a transposition
to any odd permutations.for some n.
Proof: By Cayley’s theorem we know the right regular action of G induces a
natural embedding of G in Sn, via σg, where n = |G|. The generalization to
An+2 is possible with the following construction.
Deﬁne f : G → An+2 as f (g) = σg if σg is an even permutation. In
the case that σg is an odd permutation, it follows that some cycle in a dis-
joint cycle decomposition of σg is of even length, or σg is a product of disjoint
transpositions. In any event, the order of σg is even. As such we may assign
f (g) = σg(n + 1,n + 2). As n + 1 and n + 2 are ﬁxed by Sn, this addition does
not interfere with the embedding and simply serves to make each permutation
even. □
56C15 as a Permutation Group. – True or False? A5 contains no subgroup Hint: Act on the cosets of
such a subgroup.of order 15. 10
Proof: Suppose H is a subgroup of order A5. Since [ A5 : H] = 4, it follows
A5 acts on 4 elements transitively so A5 embeds in S4. However |A5| = 60 and
|S4| = 24 which means there is a proper non-trivial kernel in A5. Yet A5 is
simple so no suitable kernel exists. □
57 C15 as a Permutation Group. Find the smallest n such thatAn contains Hint: The only group of order
15 is C15 and such a subgroup
does not embed in Sn untilS8.
a subgroup of order 15.
Example: n = 8 is required. To see, this ﬁrst we recall that the groups of
order pq are classiﬁed. As 5 ≡/ 1 (mod 3) it follows the only group of order 3 · 5
is C15. To build a permutation of order 15 requires one of two things: a cycle
of length 15, or a disjoint product of a 3 cycle and a 5 cycle. Thus we need at
least n = 8.
Whenn = 8 the element (123)(45678) has order 15 and is even so indeed we
haveC15 embedded in A8. □
58 Normal Sylow-subgroups. – True or False? Let G be a ﬁnite group, Hint: Note all Sylow- p-
subgroups are hence contained
in N (Exercise-1.53).
and let P be its Sylow-p-subgroup. If P ⊴N ⊴G then P ⊴G.
Proof: AsP is SylowG, and contained in N , it must be a Sylow- p-subgroup of
N as well. We know given any Sylow-p-subgroupQ,Q∩N is a Sylow-p-subgroup
of N by Exercise- 1.53. This means every Sylow- p-subgroup of G is completely
contained in N or otherwise the intersection would be of an order less than that
of P . However now we see that since P is normal in N it cannot be conjugate
to any other subgroups of N , so N must have a unique Sylow- p-subgroup, and
so indeed G has a unique Sylow- p-subgroup proving P is normal in G. □
59 Centers of p-groups. LetG be a ﬁnite p-group, and N ⊴G be a normal Hint: Consider the size of a
conjugacy class in N .subgroup of order p. Then N is in the center of G.
10The only group of order 15 is cyclic, and clearly now permutation on 5 letters can have
order 15. So such a subgroup is not in S5 much less A5.

26 CHAPTER 1. GROUPS
Proof: Take any element n ∈N . If N is not central then there is an element
g ∈ G which conjugates n non-trivially. If gng −1 /∈ N then N is not normal.
Thusgng −1 ∈N . This means that the conjugacy class of n is contained entirely
in a group of order p. If n = 1 then the class has order 1. Thus if n ⁄= 1 then
its conjugacy class has order less than or equal to p − 1. However all numbers
less than p are relatively prime to p, and so as all conjugacy classes must have
order dividing that of the group, the conjugacy class of n must be 1. Hence n
is central so N ≤Z(G). □
60 Centers. IfG is a ﬁnite p-group,N ⊴G, andN ⁄= 1, thenN ∩Z(G) ⁄= 1.Hint: Every p-group is nilpo-
tent. Proof: First we know from Prop-1.9.21 every p-group is nilpotent. When we
combine this with Prop-1.9.25 we have every non-trivial normal subgroup of G
intersects the center non-trivially. □
61 Centers of Products. Let H,K,N be non-trivial normal subgroups ofHint: Look at commutators
between the product. a group G, and suppose that G =H ×K. Prove that N is in the center of G or
N intersectsH,K non-trivially. Give an example where N is in the center and
does not intersect either H orK non-trivially. Give an example where N is not
in the center but intersects both H andK non-trivially. Give an example when
N is in the center and intersects both H and K non-trivially.
Proof: Suppose H ∩N = K ∩N = 1. Take a commutator from each: let
h ∈H, k ∈K and n ∈N ; then [h,n ] ∈N as N is normal, and also [ h,n ] ∈H
as H is normal, so [ h,n ] = 1 as their intersection is trivial. The same goes for
[k,n ]. Therefore N is central to all elements of H and to all elements of K, so
since HK =G it follows N is central to all elements in G, so N ≤Z(G). □
Example: D2 = ⟨a⟩ × ⟨b⟩ ∼= Z2 ⊕ Z2 11 has a normal subgroup ⟨ab⟩ which does
not intersect either product. However since the group is abelian every thing is
contained in the center.
InD6 the center is no longer the entire group but simply ⟨a3⟩ (see Exercise-
??). ⟨a3⟩, ⟨a2,b ⟩ ⊴D6 and nontrivial. ⟨a3⟩ ∩ ⟨a2,b ⟩ = 0 and ﬁnally ⟨⟨a3⟩ ∪
⟨a2,b ⟩⟩ = ⟨a2,a 3,b ⟩ =D6. Therefore D6 = ⟨a3⟩ × ⟨a2,b ⟩ ∼= Z2 ×D3. 12
The list of nontrivial normal subgroups of D6 is (Exercise- ??):
⟨a3⟩, ⟨a2⟩, ⟨a⟩, ⟨a2,b ⟩, ⟨a2,ab ⟩.
Clearly the ﬁrst non-trivially intersects ⟨a3⟩ – and it is contained in the center
(it is the center); the next four non-trivially intersect ⟨a2,b ⟩ – they all contain
⟨a2⟩. □
62 Counter Examples. – True or False? Fori = 1, 2 let Hi ⊴Gi, determineHint: Each is false.
which are true and which are false.
(a) G1 ∼=G2 and H1 ∼=H2 ⇒ G1/H1 ∼=G2/H2.
(b) G1 ∼=G2 and G1/H1 ∼=G2/H2 ⇒ H1 ∼=H2.
(c) H1 ∼=H2 and G1/H1 ∼=G2/H2 ⇒ G1 ∼=G2.
Example:
(a) Z ∼= Z and 2 Z ∼= Z ∼= 3Z but certainly Z/2Z is not isomorphic to Z/3Z as
they do not even have the same order.
11D2 is the symmetries of a rectangle.
12D6 is the symmetries of a hexagon, which contains two disjoint regular triangles whose
symmetries are D3 – hence D6 is structurally equivalent to a product of D3.

Algebra – James Wilson 27
(b) D8 ∼=D8 and D8/⟨a⟩ ∼= Z2 ∼=D8/⟨a2,b ⟩ but ⟨a⟩ is cyclic and ⟨a2,b ⟩ is not,
so they are not isomorphic.
(c) ⟨2⟩ ⊴ Z4 and ⟨(1, 0)⟩ ⊴ Z2 ⊕ Z2. Notice ⟨2⟩ ∼= Z2 ∼= ⟨(1, 0)⟩, and Z4/⟨2⟩ ∼=
Z2 ∼= Z2 ⊕ Z2/⟨(1, 0)⟩; however, Z4 is cyclic while Z2 ⊕ Z2 is not, so they
are not isomorphic.
□
63 Solvable Groups. Let G be a ﬁnite group. If G is solvable, then Hint: Consider the last term
in the derived series.G contains a non-trivial normal abelian subgroup. If G is not solvable then it
contains a normal subgroup H such that H ′ =H.
Proof: Consider the derived series of G. First notice G(i) is normal in G for
all i. In the ﬁrst case G′ is normal. Now suppose G(i) is normal in G. Then
taking any generator [ a,b ] ∈ G(i+1) and any x ∈ G, it follows a,b ∈ G(i) so
xax−1,xbx −1 ∈G(i) since G(i) is normal. Moreover now we see:
x[a,b ]x−1 =xaba−1b−1x−1 =xax−1xbx−1xa−1x−1xbx−1 = [xax−1,xbx −1].
SinceG(i+1) contains all commutators ofG(i) it must therefore containx[a,b ]x−1.
SinceG(i+1) is closed under conjugation of generators it is in fact closed to con-
jugation of all elements. Therefore G(i+1) is normal in G so by induction the
derived series is a normal series.
IfG is solvable then the series must terminate at some n. Thus the commu-
tator of G(n−1) is trivial. Therefore G(n−1) is abelian and thus G has a normal
abelian subgroup.
If G is not solvable, then the series must not terminate. However the group
is ﬁnite so the sequence must stabilize at some G(n); that is: ( G(n))′ =G(n) for
some n and G(n) ⁄= 1. □
64 Subgroups of Cp ×Cp. Letp be prime. Show the number of subgroups Hint: Number of generator in
each copy of Cp is p − 1.of Cp ×Cp is p + 3.
Proof: Given any (a,b ) ∈ Cp ×Cp it follows (a,b )p = (ap,bp) = (1, 1). Thus
every non-trivial element generates a subgroup of order p. Furthermore, each
such subgroup contains p − 1 non-trivial elements. Since every proper subgroup
ofCp ×Cp must have order p, it follows this counts all proper subgroups. There
are, therefore, p2 − 1 elements in proper subgroups of Cp ×Cp each which con-
tains p − 1 elements for a total of p2−1
p−1 =p + 1 proper subgroups. Adding the
two trivial groups we get our formula. □
65 Automorphisms. Let G be a group, and suppose |Aut(G)| = 1. Prove Hint: Treat in cases: G non-
abelian, abelian, and G as a
group of involutions.
that G has at most two elements.
Proof: If G is non-abelian then there exists elements g,h ∈ G such that
gh ⁄=hg so indeed ghg −1 ⁄=h. However conjugation is always an automorphism
of G, so we are now convinced there is a non-trivial automorphism of G.
Now suppose G is abelian.
IfG has an element that is not of order 2, then the automorphism f (x) = −x
is non-trivial. We see this is indeed an automorphism since it is clearly bijective
– inverses are unique – and as G is abelian
f (x +y) = −(x +y) = −x + −y =f (x) +f (y).
Now consider the case where G is a group of involutions. As G is still abelian,
Z acts on G but 2 Z annihilates G so indeed G is a Z2 vector space. Thus
G ∼= Z2 ⊕ · · · ⊕ Z2 = Fn
2.

28 CHAPTER 1. GROUPS
Thus G has GLn(F2) as its automorphism group which is non-trivial unless
n = 1. Therefore |Aut(G)|> 1 unless |G| ≤ 2. □
66 Nilpotency of order 18. – True or False? Every group of order 18 isHint: Consider the dihedral
groups. nilpotent.
Example: False. In Exercise- 1.51 we saw Dn was nilpotent only if n was a
power of 2. Hence D18 is not nilpotent and it is a group of order 18. □
67 Diagonal Embedding. Let G1, and G2 be ﬁnite groups. Is it trueHint: Consider C2 ×C2.
that every subgroup of G1 ×G2 is of the form H1 ×H2, where H1 ≤ G1 and
H2 ≤G2? What if additionally ( |G1|, |G2|) = 1?
Example: The ﬁrst assumption is false. We see this even with the smallest
example C2 ×C2. Here the subgroup ⟨(1, 1)⟩ is isomorphic to C2 but its left
and right projections are C2, suggesting it should be C2 ×C2, which it is not.
Therefore the subgroup cannot be split. □
However adding the condition of relatively prime is suﬃcient. Proof: Suppose
|G1| and |G2| are relatively prime. Let H ≤G1×G2. If we take any (h1,h 2) ∈H
we observe the following:
(h1,h 2)|G1| = (1,h |G1|
2 ) = (1,h ′
2).
Since the order of |G1| is relatively prime to |G2| it must also be relatively
prime the order of any element h2 inG2; thus, h′
2 has the same order as h2 and
moreover generates h2 – say by a power k. Therefore:
(h1,h 2)|G1|k = (1,h ′k
2 ) = (1,h 2).
Therefore,π2(H) is naturally embedded in H as 1 ×π2(H). The same goes for
π1(H).
ClearlyH1 =π1(H)×1 andH2 = 1×π2(H) split in H, and they are normal
inH because they are equivalent to G1 ∩H andG2 ∩H and we know both G1
andG2 are normal. Therefore H is the internal direct product of H1 andH2. □
68 Centrality in p-groups. – True or False? Any element of order p in aHint: Consider D8.
ﬁnite p-group is central.
Example: In D8 every ﬂip is of order 2, yet no ﬂip is central. □
69 Classiﬁcation of Sylow-subgroups. Let p be a prime and G be aHint: Consider the action of
G on the cosets of H. ﬁnite simple group having a subgroup H of index p. Find the isomorphism type
of a Sylow-p-subgroup of G.
Proof: Since G acts transitively on the subgroup’s cosets we have a map
G → Sp. However G is simple so it is contained in Ap. Now we see that the
order of G is less than or equal to p!/2. This means p|G but p2 ∤ G and that
p (and p is the largest prime dividing the order of G.) Now we know that a
Sylow-p-subgroup has order p so it is simply Cp. □
70 Groups of order 175. Classify the groups of order 175.Hint: Use Sylow theory.
Proof: Note that 175 = 5 2 · 7; thus, the third Sylow theorem tells us there is
precisely one Sylow 7-subgroup, of order 7, and is consequently normal. At the
same time, since 7 ≡/ 1 (mod 5) we know the number of Sylow-5-subgroups is
1 as well. Hence G has two normal subgroups that intersect trivially because

Algebra – James Wilson 29
their orders are relatively prime, and whose product is the entire group. So G
is a direct product of its Sylow subgroups. Therefore using the classiﬁcation of
the groups of order p2 we may say with certainty the groups of order 175 are
C7 ×C25, C 7 ×C5 ×C5.
□
71 Free-Abelian Groups. Let F be a free group with basis X = Hint: Recall a basis of a free-
abelian group is linearly inde-
pendent.
{x1,...,x n}. Then F/F ′ ∼= Z ⊕ · · · Z, n-copies.
Proof: Deﬁne f : F/F ′ → Zn by f (xiF ′) = ei where {e1,...,e n} is the
standard basis of the free-abelian group Zn. Since F/F ′ is abelian, the relations
commutative relation holds across f so by v. Dyck’s theorem we know f is
a homomorphism. Moreover, {e1,...,e n} spans Zn so indeed f is surjective.
Finally suppose f (aF ′) = ⃗0. As F is free we may take a to be generated from
the basis so that:
aF ′ =xi1 · · ·xijF ′ =xd1
1 · · ·xdn
n F ′
for appropriate ik’s and di’s – with the last step made possible by the commu-
tator relations in F ′. As such we have
⃗0 = f (aF ′) = f (xd1
1 · · ·xdn
n F ′) = f (xd1
1 F ′ · · ·xdn
n F ′) = d1e1 + · · · +dnen
However Zn is a free-abelian group so the ei’s are linearly independent so that
their sum is 0 only if each coeﬃcient is 0; thus, di = 0 for all i. Now we pull
this result back to say
aF ′ =x0
1 · · ·x0
nF ′ =F ′.
Hence the kernel is trivial so our homomorphism is an isomorphism. □
72 Free Groups. Let X ⊆Y . Show F (X) ≤F (Y ). Hint: Use the universal prop-
erty of F (X) to create a nat-
ural injection.
Proof: We make use of the canonical embedding:
X /d31 /d127 i /d47/d47/d127 /d95
ιX
/d15/d15
Y/d127 /d95
ιY
/d15/d15
F (x)
f /d43/d51F (Y ).
f is given by applying the universal property on F (x) with the map ιYi. Now
we verify that f is injective.
1 = f (ιX (xi1) · · ·ιX (xim ))
= ιY (i(xi1)) · · ·ιY (i(xim ))
= ιY (xi1) · · ·ιY (xim ).
Now recall that the image lies in F (Y ) which is free of all but the necessary
group relations. Thus
1 = ιY (xi1) · · ·ιY (xim )
only if there is a path to reduce the letters to the empty string. This path
depends only on the arrangement of the indices ik. So we pull this path back
to F (X) and ﬁnd it too reduces
ιX (xi1) · · ·ιX (xim ) = 1.
Thus the kernel is trivial. □

30 CHAPTER 1. GROUPS
73 Symmetries of the Tetrahedron. Find the group of rotations and the Hint: The axes of rotation or
either through a face and the
opposing vertex, or at the cen-
ter of the tetrahedron.
full group of symmetries of a regular tetrahedron.
Example: There are four vertices on the regular tetrahedron so the action on
the vertices being suﬃcient to describe the symmetries tells us the symmetries
lie in S4. When we ﬁx an axis of rotation through the center of a fact and
the opposing vertex we see a rotation of order 3, so we attain all 3 cycles and
thus a copy of A4 – as the 3-cycles generate An in Sn. This is thus the group
of rotations as it includes the rotations ( ab)(cd) which are those whose axis of
symmetry is the center of the tetrahedron.
For the full group of symmetries we must convince ourselves that there are
no other symmetries. If we add any odd permutation we will acquire all of S4
as our symmetries. Thus consider a permutation ( ab). If two adjacent vertices
are ﬁxed then the edge between them is ﬁxed and thus the triangles that share
this edge are ﬁxed. This means two of the 4 triangle faces are ﬁxed, and thus
the edges of these triangles are also ﬁxed. This means indeed all the triangles
are ﬁxed as the two triangles already ﬁxed share two edges with the remaining
two triangles. Finally, unlike the cube, any two vertices are adjacent so this is
always the case. Hence, the symmetries do not contain a permutation of the
form (ab) so they cannot be all of S4. Since they must contain A4 – the group
of all rotations – we are forced to conclude the full symmetry group is precisely
the group of rotations: A4. □
74 Conjugation in S5. Describe the conjugacy class of A5 and S5.Hint: Permutations in Sn are
conjugate if they have the
same cycle structure.
Example: In Sn permutation with the same cycle structure are conjugate. So
inS5 we have the following conjugacy classes: (let a,b,c,d,e be distinct elements
from {1, 2, 3, 4, 5})
[()], [(a,b )], [(a,b,c )], [(a,b,c,d )], [(a,b )(c,d )],
[(a,b,c,d,e )], [(a,b,c )(d,e )],
with respective orders: 1 , 10, 20, 30, 15, 24, 20.13 The sum is 120 so we have
accounted for all the permutations.
Now in An we are not privileged to have as strong a statement as we have
inSn. First of all the size of the conjugacy classes must divide the order of the
group, so we can only select from 1,2,3,4,5,6, 10, 12, 15, 20, 24, or 30. To help
us narrow the study consider any class order less than 5. Then conjugation acts
transitively on this class so that we require a homomorphism A5 → Sk, with
k< 5. Since A5 is simple this requires the action to be trivial – which it is not
unless the class is of order 1. However the center of A5 is trivial so the only
class of order less than 5 is [()]. These leaves us with the possible orders 5,6,
10, 12, 15, 20, 24, and 30. Note moreover that this applies not only to the size
of conjugacy classes of elements but also of subgroups.
We observe that in A4, the permutations ( a,b )(c,d ) are all conjugate – for
instance by (a,b,c ) we see it is conjugate to ( a,d )(b,c ) and from ( a,c,b ) we get
(a,c )(b,d ). Now we put this to use. As ( a,b )(c,d ) ﬁxes e, it must be in Ae
4
which is the copy of A4 in A5 which ﬁxes e. Hence all copies of A4 in A5 have
disjoint 2 by 2 cycles. By the above reasoning we know that the subgroups Ai
4
13 The number of cycles of length r from n letters is given by
nJr = n!
(n − r)!r .
For k disjoint copies of length r from n letters simply notice this is produced from a cycle of
length kr taken to the r/k power.

Algebra – James Wilson 31
(of which there are ﬁve because we can only ﬁx one of the ﬁve letters at a time)
are conjugate. Therefore indeed the conjugation extends to the 2 by 2 cycles so
we may now conclude that all 2 by 2 cycles are conjugate in A5.
Now we are left with 3 cycles and 5 cycles. We must partition the total 20
3-cycles and 24 5-cycles into conjugacy classes whose orders are 5, 6, 10, 12, 15,
20, 24, 30. In A4 the 3-cycles break into 2 conjugacy classes each of size 4, since
the the elements are not central, 8 does not divide 12, and there is no subgroup
of index 2 so there is no centralizer of this order. Thus in A5 the 3-cycles are
at least in classes of size 4. However the Ai
4 subgroups are conjugate so we
must extend this conjugation to the classes in A4 to see that we either connect
them all into 2 classes, or into 1. However we notice the centralizer of ( a,b,c ) is
contains (a,b,c ) and (d,e ) so it must have order at least 6 which forces use to
conclude the class size is no larger than 10. Yet it must be exactly 10 so that
there are only 2 classes.
This also tells us about ( a,b,c )(d,e ). Since the ﬁrst component is conjugate
only in groups of 10, then we must have these conjugate in groups of 10 or 5. If
it is 5 then the centralizer must have order 12 which would make it A4 (no other
order 12 group lies in A5). Yet the centralizer must contain the element which
would mean A4 has an element of order 6 which it does not. So the elements
(a,b,c )(d,e ) are arranged in two classes of order 10 each.
Finally, the 30 5-cycles must be arranged. The centralizer must have order
at least 5 which requires the classes have order no greater than 12. This means
either 2 classes of order 12, or 4 classes of order 6, etc – we know the arrangement
to be homogeneous because all centralizers are conjugate and so the their indices
are equal. If it is 6 then we require the copy of D10 inA5 centralizer its 5-cycles
– which it does not – the center of D10 is trivial. Hence it must be 12 as the
centralizer must be C5.
So the conjugacy classes of A5 are: a single [()] of order 1, 2 classes of 3-
cycles, each of order 10, 1 class of 2 by 2 cycles, and of order 15, 2 classes of
order 10 of 3 by 2 cycles, and 2 classes of order 12 each of 5-cycles. □
75 Dihedral Groups. – True or False? D12 ∼=S3 ×C2. Hint: Consider the regular tri-
angles embedded in a regular
hexagon.
Proof: Geometrically the proof is simple: the hexagon has two regular trian-
gles inscribed within. This gives two copies of D6 ∼= S3 in D12, both of index
2 so they are normal. Now consider the rotation a3 which visibly has order 2.
This rotates one regular triangle onto the other. In particular this tells us it
does not intersect the copies of D6. As a3b = ba3 we see a3 is central so this
C2 subgroup is normal. Hence we have two normal subgroups that intersect
trivially and whose join is the entire group. Hence we have an internal direct
product so indeed: D12 ∼=D6 ×C2. □
76 Sp generators. Let p be prime g be any p-cycle in Sp and h be any Hint: Show that all transpo-
sition can be determined from
the cycle. Make sure to use
the primality of p.
transposition in Sp. Prove ⟨g,h ⟩ =Sp.
Proof: Takeσ = (a0,...,a p−1) and τ = (a0,ai) (we can rotate the numbers
in σ so that the ﬁrst terms agree, thus choice imposes nothing outside the
hypothesis). We also know
σjτσ −j = (aσj (1),aσj (i))
where i + 1 i modulo p. Since p is prime we know the cycles remain the same
length as we take powers:
σj = (a1,aj,a 2j,... ).

32 CHAPTER 1. GROUPS
Together we see we can construct the transpositions:
(a0,ai), (a1,ai+1),..., (ap−1,ai+p−1)
Since we have p distinct transpositions so they generate a symmetric group. Yet
we also have that they are transitive on all p elements so they must generate
Sp. □
77 Dihedral Groups. LetD2n be the dihedral group of order 2 n. For which
values of n:
(a) The center of D2n is trivial?
(b) All involutions in D2n are conjugate to each other?
(c) D2n is a direct product of two proper subgroups?
(a) Proposition 1.0.5 Letn> 2. If n is even then the center of D2n is ⟨an/2⟩,
and when n is odd the center is trivial.
Remark 1.0.6 When n = 2 , D2n is simply the Klein 4-group C2 ×C2
which will have as its center all of D2n. When n = 1 , D2 ∼= C2 so we
restrict our attention to n> 2.
Proof: To see this we make use of the free presentation:
D2n = ⟨a,b | an =b2 =e,ba =a−1b⟩
and D2n has order 2n. Notice this last relation gives D2n the normal form
aibj.
Suppose aib is central; then given any ak it should follow:
ai−kb = (aib)ak =ak(aibj) = ai+kb.
However this implies a−k =ak for all k = 1,...,n . Since n> 2 this will not
be true for all k. Therefore the center of D2n may not contain an element
of the form aib.
Suppose ai is central. Then for all ajb it follows:
ai+jb =ai(ajb) = (ajb)ai =aj−ib,
which requires aj+i =aj−i or simply that ai =a−i. Of course this requires
2|n and that i =n/2. Now we check; let 2 |n, then:
an/2(ajb) = an/2+jb =ajan/2b =ajba−n/2 = (ajb)an/2.
Since ai is clearly central to all aj we may conclude the center of D2n is
⟨an/2⟩ when n is even and trivial otherwise. □
(b) Proposition 1.0.7 Letn> 2. If n is even then the involutions break into
conjugacy classes of:
{an/2}, {b,a 2b,...,a n−2b}, {ab,a 3b,...,a n−1,b }.
If n is odd then we have all involutions conjugate to each other.

Algebra – James Wilson 33
Proof: We saw above that when n is even, an/2 is central. Hence it is in
its own conjugacy class. For the rest, when we conjugate we get:
aiba−i =a2i; ai(ab)a−i =a2iab =a2i+1b.
Hence we have the above conjugacy classes when n is even. When n is odd
we see that 2 i will eventually span all of Zp so indeed the class becomes all
involutions. □
(c) Proposition 1.0.8 Given (2,m ) = 1 and n ≥ 1, it follows
D4m ∼=D2m ×C2.
Otherwise D2n does not split as a non-trivial direct product.
Proof: TakeD2n =H ×K for subgroups H and K of D2n. As such both
must be normal subgroups of D2n. This means they are either subgroups
of the full rotation group or they are of index 2 – since all subgroups of D2n
are copies of D2i and are conjugate unless the index is 2. If both H andK
are rotation groups then their join will not be all of D2n so one must be a
copy of D2 n
2 which requires furthermore that 2 |n. As such we now see the
other group must have order 2, and so it must be C2 and so it is the center
ofD2n as it is the only normal involution group. In the end we see that the
intersection of D2 n
2 and Z(D2n) is trivial only when n
2 is relatively prime
to 2. So we conclude that n = 2m with (2,m ) = 1.
Now suppose these conditions are met: Z(D4m) intersect D2m is trivial and
their join is all of D4m. Moreover both are normal so indeed D2n is the
internal direct product of these two groups. □

34 CHAPTER 1. GROUPS

Chapter 2
Fields
1 T/F Galois Group Order. . . . . . . . . . . . . . . . . . . 37
2 Countable Extensions. . . . . . . . . . . . . . . . . . 37
3 Countability of A. . . . . . . . . . . . . . . . . . . . 37
4 T/F Algebraic Towers. . . . . . . . . . . . . . . . . . . . . 37
5 T/F Simple Extensions. . . . . . . . . . . . . . . . . . . . 37
6 Irreducible Polynomials. . . . . . . . . . . . . . . . . 37
7 T/F Normal Transitivity. . . . . . . . . . . . . . . . . . . 38
8 T/F Field Isomorphisms. . . . . . . . . . . . . . . . . . . 38
9 Transcendental Extensions. . . . . . . . . . . . . . . 38
10 T/F Domain Extensions. . . . . . . . . . . . . . . . . . . 39
11 Algebraic Extensions. . . . . . . . . . . . . . . . . . 39
12 Perfect Fields. . . . . . . . . . . . . . . . . . . . . . . 39
13 Transitive Actions on Roots. . . . . . . . . . . . . . . 40
14 Inﬁnite Field Multiplication. . . . . . . . . . . . . . . 40
15 Partial Splits. . . . . . . . . . . . . . . . . . . . . . . 41
16 T/F Transcendental Galois Groups. . . . . . . . . . . . . 41
17 Field Extensions. . . . . . . . . . . . . . . . . . . . . 42
18 Normal Extensions. . . . . . . . . . . . . . . . . . . . 43
19 Extension Degrees. . . . . . . . . . . . . . . . . . . . 44
20 T/F Field Monomorphisms. . . . . . . . . . . . . . . . . . 44
21 Galois Groups. . . . . . . . . . . . . . . . . . . . . . 45
22 Finite Fields. . . . . . . . . . . . . . . . . . . . . . . 47
23 T/F pk-th roots in Finite Fields. . . . . . . . . . . . . . . 48
24 T/F Normal Extensions of C. . . . . . . . . . . . . . . . . 48
25 Rational Function Fields. . . . . . . . . . . . . . . . 48
26 T/F Normal Extensions. . . . . . . . . . . . . . . . . . . . 48
27 Separable Transitivity. . . . . . . . . . . . . . . . . . 48
28 Counting Polynomials. . . . . . . . . . . . . . . . . . 49
29 Intermediate Finite Fields. . . . . . . . . . . . . . . . 49
30 Splitting Fields. . . . . . . . . . . . . . . . . . . . . . 49
31 Simple Extensions. . . . . . . . . . . . . . . . . . . . 49
32 Squares in Finite Fields. . . . . . . . . . . . . . . . . 50
33 Simple Transitivity. . . . . . . . . . . . . . . . . . . . 50
34 . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 50
35 . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 50
37 . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 50
38 . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 51
35

36 CHAPTER 2. FIELDS
40 . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 51
41 . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 51
42 . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 52
44 . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 52
45 . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 52
46 . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 52
47 . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 52
48 . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 52
49 . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 53
50 . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 54
51 . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 54
52 . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 54
53 . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 55
54 . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 55
56 . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 56
57 . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 57
58 . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 58
59 . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 58
60 . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 58
68 . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 59
72 . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 59
77 . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 59
78 . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 59
80 . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 60
83 . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 60
84 . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 60
85 . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 60
86 . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 61
88 . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 61
89 . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 61
91 . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 62
92 . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 62

Algebra – James Wilson 37
1 Galois Group Order. – True or False? The Galois group of Q(
3√
2) over Hint: Find the degree of the
minimal polynomial.Q has order 3.
Proof: True. We notice
3√
2 is a root of x3 − 2, and
x3 − 2 = (x −
3√
2)(x2)
so irr(Q;
3√
2) = x3 − 2. The minimal polynomial x3 − 2 tells us the degree of
the ﬁeld extension Q(
3√
2)/Q is 3. Therefore the order of the Galois group is 3.
□
2 Countable Extensions. If the extension K/k is algebraic and k is Hint: Note that a count-
able union of countable sets is
countable.
countable then K is also countable.
Proof: Since k is countable, the ring k[x] is countable as it is in one-to-one
correspondence with the countable union ⋃
i∈Nki of countable sets. Thus there
are a countable number of roots as each element in k[x] has only ﬁnitely many
roots. Since K is algebraic of k, every element in K is a root of some polynomial
in k[x] so it is a subset of the countable number of all roots of k. □
3 Countability of A. The ﬁeld A – all algebraic elements over Q – is Hint: Use Exercise- 2.2.
countable.
Proof: Since Q is countable and by deﬁnition A/Q is an algebraic extension,
it follows from Exercise- 2.2 that A is countable. □
4 Algebraic Towers. – True or False? If F/K/k are ﬁeld extensions with Hint: Choose any element
and show its extension is ﬁnite
over k.
F/K and K/k algebraic, then F/k is also algebraic.
Proof: Given any element α ∈ F , α is algebraic over K so there exists an
irreducible polynomial anxn + · · · +a0, ai ∈K to which α is a root. Moreover,
K is algebraic over k so each ai is algebraic over k. Thus in fact k(a0,...,a n)
is algebraic over k and k(a0,...,a n,α ) is algebraic over k(a0,...,a n). Notice
[k(a0,...,a n,α ) : k(a0,...,a n)] = n as the irreducible polynomial has degree
n, and k(a0,...,a n) is a ﬁnite extension also of k as it is a ﬁnite number of
simple extensions. Thus the degree [ k(a0,...,a n,α ),k ] is ﬁnite and thus alge-
braic. Therefore α is algebraic over k. Since we began by selecting any α ∈F
it follows all of F is algebraic over k. □
5 Simple Extensions. – True or False? The extension Q(i,
√
5) is simple. Hint: Compare it to Q(i +√
5)Example: Consider Q(i +
√
5). Notice ( i +
√
5)2 = −1 + 2i
√
5 + 5 = 4 + 2i
√
5,
and so in fact i
√
5 is in the extension as −4, 1/2 ∈ Q. Thus 1 +i
√
5 ∈ Q(i+
√
5).
Now take
(i +
√
5)(1 +i
√
5) = i + 5i +
√
5 −
√
5 = 6i.
As 1/6 ∈ Q it follows i ∈ Q(i +
√
5) and so −i is as well allowing us to conclude√
5 ∈ Q(i +
√
5) so that Q(i,
√
5) ≤ Q(i +
√
5) Since the reverse inequality is
trivial we may actually assert Q(i,
√
5) = Q(i +
√
5) so it is visibly a simple
extensions. □
6 Irreducible Polynomials. Let p be prime. Then the polynomial Hint: Use Eiseinstein’s Crite-
rion.f (x) = 1 + x + · · · +xp−1 in Q[x] is irreducible.
Proof: If p = 2 then f (x) = 1 + x which is irreducible as it is a monomial.
Now let p> 2.
This follows from a clever application of the Eisenstein Criterion. If we
substitute 1 + x for x in f (x), (by the evaluation homomorphism) we shift all

38 CHAPTER 2. FIELDS
roots to the left by 1 – formally any root α of f (x), yields the root α − 1 of
f (1 +x); thus if f (1 +x) is irreducible then so is f (x), by the contrapositive of
the statement.
f (1 +x) = 1 + (1 + x) + · · · + (1 +x)p−1 =a0 +a1x + · · · +ap−1xp−1.
Recall
(1 +x)n = 1 +
(n
1
)
x + · · · +
(n
k
)
xk + · · · +xn
so that
ai =
p−1∑
j=i
(j
i
)
=p
(p − 1
i
)
, i<p − 1.
Firstap−1 = 1. Also p divides each ai, 0 ≤i<p − 1 and p2 ∤a0 =p. So by the
Eisenstein criterion f (x + 1) is irreducible. □
7 Normal Transitivity. – True or False? IfF/K/k are ﬁeld extensions withHint: Consider the statement
in terms of Galois groups. F/K and K/k normal, then F/k is also normal.
Example: Consider Q(
4√
2)/Q(
√
2)/Q. As ±
4√
2 is a root of x4 − 2 with the
other two roots being complex, we do not have all the roots of x4 − 2 in Q(
4√
2)
proving the extension Q(
4√
2)/Q is not normal.
However at the same time notice that ±
√
2 are the only roots of x2 − 2 so
Q(
√
2) is a splitting ﬁeld for x2 − 2 so it is a normal extension over Q. Also,
±
4√
2 are the only roots of x2 −
√
2 over Q(
√
2), so indeed Q(
4√
2) is a splitting
ﬁeld over Q(
√
2) of x2 −
√
2 and hence the extension is normal.
In the end we have a tower of normal extensions but the overall extension is
not normal so we have disproved the transitivity of normality. 1 □
8 Field Isomorphisms. – True or False? Q(i) and Q(
√
2) are isomorphicHint: Consider Q as ﬁxed and
that the squares of the square
roots are distinct.
ﬁelds.
Example: First we construct the irreducible polynomials associated with the
extensions. Certainly i is a root of the unique monic lowest degree irreducible
polynomialx2 + 1 in Q. Likewise x2 + 2 is the unique monic irreducible polyno-
mial with root
√
2 – both so because we require even, positive, degree to reverse
the squareroot function so no lower degree polynomial will suﬃce.
Now to conclude they are not isomorphic consider constructing a Q-isomorphism.
Let ϕ = idQ. From Thm-2.3.14 we know there exists a ﬁeld isomorphism
ˆϕ : Q(i) → Q(
√
2) extending ϕ if and only if ϕ(irr(i, Q)) = irr(
√
2, Q).
But notice a ﬁeld isomorphism (indeed homomorphism) must send 1 to 1, so
ϕ(x2 + 1) = x2 + 1 ⁄=x2 + 2. Thus we cannot extends the isomorphism ϕ to be
between Q(i) and Q(
√
2).
Well this does not preclude the existence of an isomorphism between Q(i)
and Q(
√
2) which is not a Q-isomorphism. However if such an isomorphism ϕ
exists then notice it too is required to map 1 to 1. This then forces ϕ|Z =idZ,
as 1 generates Z. Moreover this then requires
1 = ϕ(1) = ϕ(n · 1/n) = ϕ(n)ϕ(1/n) = nϕ(1/n),
so 1/n =ϕ(1/n). But then notice in fact
ϕ(a/b) = ϕ(a)ϕ(1/b) = a/b;
1Notice that a splitting ﬁeld for x4 − 2 has Galois group D8 which is the ﬁrst counter
example for normal transitivity in groups.

Algebra – James Wilson 39
thus, ϕ|Q = idQ. Hence all isomorphism must be Q-isomorphisms, but none
such exist so there are in fact no isomorphisms between Q(i) and Q(
√
2). □
9 Transcendental Extensions. If β is algebraic over k(α) and β is Hint: Construct a new poly-
nomial over k(β) which anni-
hilates α from a polynomial
killing oﬀ β over k(α).
transcendental over k, then α is algebraic over k(β).
Proof: Givenβ is algebraic over k(α) it follows there exists some polynomial
f (x) = a0 +a1x + · · · +anxn in k(α) to which β is a root. Moreover, since β
is transcendental over k, not all of the coeﬃcients ai are in k, or otherwise the
polynomial would lie in k[x] make β algebraic over k. Thus for some ai, some
positive power of α is exhibited. If we substitute all instances of α inf (β) with
y, and call this f ′(y), thenf ′(y) is a polynomial in x for whichf ′(α) = f (β) = 0;
hence,α is a root of some polynomial of k(β) provingα is algebraic overk(β). □
10 Domain Extensions. – True or False? If K/k is algebraic and D is an Hint: Showk(a) ≤D for any
a ∈D.integral domain such that k ≤D ≤K, then D is a ﬁeld.
Proof: Take any a ∈ D. Since a ∈ K it follows a is algebraic over k. Hence
k(a) = k[a,a 2,...,a n] is an algebraic extension. Notice k(a) simply consists of
all powers, sums, and products of elements in k and and of a, all of which are
inD as well, so k(a) ≤D. However, k(a) is a ﬁeld so there exist an a−1 ∈k(a).
But this requires then that a−1 ∈ D so that D is closed to inverses. Thus in
fact D is an integral domain. □
11 Algebraic Extensions. Let K/k be a ﬁeld extension. This extension Hint: Use the ﬁniteness of
an algebraick(a) extension for
surjectivity. For the converse
use the contrapositive.
is algebraic if and only if for every intermediate ﬁeld F every k-monomorphic
from F to F is in fact a k-automorphism of F .
Proof: Suppose K/k is algebraic and let F be an intermediate ﬁeld. It follows
for every α ∈ F , that α is algebraic so that in fact [ k(α) : k] is ﬁnite. Thus
given any monomorphism ϕ :F →F , it is clear ϕ|k(α) is also a monomorphism,
and as such it has a trivial kernel. Pick any basis {e1,...,e n} of k(α) over k
and consider {f (e1),...,f (en)}. Take any ai ∈k, where
f (a1e1 + · · · +anen) = a1f (e1) + · · · +anf (en) = 0.
Since the kernel is trivial, it follows a1e1 + · · ·anen = 0 but as {e1,...,e n} is a
basis we require ai = 0 for all i; hence, {f (e1),...,f (en)} is linearly indepen-
dent. As k(α) over k has dimension n it follows this is in fact a basis, so ϕ|k(α)
is an automorphism of k(α) as it is now seen to be onto k(α).
Now suppose for some α ∈F thatα /∈ϕ(F ). Then certainly ϕ|k(α) is not an
automorphism of k(α) which is a contradiction of our earlier work. Therefore ϕ
is surjective and thus it is an automorphism of F .
For the converse consider the contrapositive. Let τ ∈K be transcendental over
k. As such we know {1,τ,τ 2,... } is a basis of the extension k(τ )/k. So deﬁne a
map ϕ(τ ) = τ 2. This determines a unique homomorphism where {1,τ,τ 2,... }
maps to {1,τ 2,τ 4,τ 6,... }. As this new set is still linearly independent it follows
the map in injective, and, moreover, 1 maps to 1, so it is a k-monomorphism.
Finally as τ is not in the image it is not an automorphism of k(τ ). □
12 Perfect Fields. A ﬁeld F is called perfect if every irreducible polynomial Hint: Cite the canonical form
for separable polynomials.overF is separable. Show that a ﬁeld F of characteristic p is perfect if and only
if every element of F has a pth root in F . Show that every ﬁnite ﬁeld is perfect.
Proof: [Rot02, Prop. 6.79] Suppose F is a perfect characteristic p ﬁeld. For
everya ∈F there is a polynomial xp −a. Since F is perfect, xp −a is separable,

40 CHAPTER 2. FIELDS
meaning it does not have multiple roots in a splitting ﬁeld. However notice it
carries the canonical form of an inseparable polynomial and is in a characteristic
p ﬁeld. Then to avoid a contradiction, xp −a must not satisfy the hypothesis
of this result (Prop-2.6.18), that is, that xp −a must be reducible. Therefore
there exists a pth root of a in F .
Now suppose a ﬁeld F has characteristic p and each element contains a pth
root in F . The only possible irreducible inseparable polynomials take the form:
f (x) = a0 +a1xp + · · · +anxpn.
Since every element of F has a pth root we may take each ai = bp
i for some
bi ∈F . Moreover, we may now express f (x) as:
f (x) = bp
0 +bp
1xp + · · · +bp
nxpn
= bp
0 + (b1x)p + · · · + (bnxn)p
= ( b0 +b1x + · · ·bnxn)p.
(As we are in a ﬁeld of characteristic p, the Freshman’s Dream applies for the
last step.) Since f (x) is visibly reducible, it follows all irreducible polynomials
overF are separable, and so F is perfect.
Every ﬁnite ﬁeld has prime characteristic, say p for a given ﬁeld F . Notice
that x ↦→ xp is ﬁeld homomorphism when F has characteristic p (Freshman’s
Dream coupled with rules of exponents.) So it is a monomorphism, as 1 ↦→ 1,
and furthermore by the pigeon-hole-principle it follows it is surjective; therefore
it is an isomorphism which simply means F =Fp and every element has a pth
root, so F is perfect. □
13 Transitive Actions on Roots. Letf ∈k[x],K/k be a splitting ﬁeld forHint: Consider the roots
forming a basis of the exten-
sion.
f overk, and G =Gal(K/k). Show that G acts on the set of roots of f . Show
thatG acts transitively if f is irreducible. Conversely, if f has no multiple roots
and G acts transitively then f is irreducible.
Proof: Takeσ,τ ∈G. Since f splits in K it follows there are α,αi ∈K such
that
f (x) = α(x −α1) · · ·(x −αn),
and also that K =k(α1,...,α n). Since each automorphism of G is a function,
the action of G on {α1,...,α n} deﬁned as σ ·αi = σ(αi) is well-deﬁned. No-
tice σ(τ (αi)) = ( στ )(αi), by the fact that multiplication in G is composition.
Also the identity map leaves all elements invariant; thus, G does indeed act on
{α1,...,α n}.
When f is irreducible, all the roots of f are outside k. As K is a splitting
ﬁeld, it follows it is normal and ﬁnite. Thus applying Prop-2.7.8, it follows there
exists an element σ ∈ G, for each ( i,j ), such that σ(ai) = aj. That is to say
that G acts transitively.
Finally, iff has no multiple roots and G acts transitively,K remains a split-
ting ﬁeld of f soK/k is still normal and ﬁnite; moreover, with no multiple roots
it is a separable extension. Now applying Coro-2.7.15 we may assert G has the
order n. Since G acts transitively on n elements, it follows every non-trivial
element acts non-trivially on K. If any root αi actually lies in k, then G must
act trivially on this element – for G is the set of all k-automorphisms of K. To
avoid this contradiction we require each αi be outside k; thus, f is irreducible
as it has no root in k. □

Algebra – James Wilson 41
14 Inﬁnite Field Multiplication. Prove that if F is an inﬁnite ﬁeld, thenHint: Treat in cases: charac-
teristic 0 or p. its multiplicative group F × is never cyclic.
Proof: If F has characteristic 0, then Q is embedded in F , and so Q× lies in
F ×. Notice 2 and 3 are relatively prime, so Q× is not cyclic, and hence neither
is F ×.
Suppose F has characteristic p; then the prime subﬁeld is isomorphic to Zp.
IfF × is to be cyclic, it most certainly is inﬁnite, so it is isomorphic to Z. How-
ever, Z is torsion free and Z×
p is nothing but torsion. F × is acyclic. □
15 Partial Splits. Let K/k be a normal ﬁeld extension and f be an Hint: PENDING:
irreducible polynomial over k. Show that all irreducible factors of f inK[x] all
have the same degree.
Proof: Since f (x) is irreducible over k, it follows f (x) = a(b(x)) for some
a(x),b (x) ∈ k[x] where a(x) is irreducible over k (or else f (x) would not be)
and has a root in K – otherwise it would have no proper factors in K either.
However,K/k is normal, so a(x) has all its roots in K so it splits in K as follows:
a(x) = α(x −α1) · · ·(x −αm).
Consequently
f (x) = α(b(x) −α1) · · ·(b(x) −αm).
Suppose b(x) −α1 is reducible. Consider the k-automorphism σ sending
α1 to αj. We know σ exists because both α1 and αj are roots of the same
irreducible polynomial, and furthermore we know the automorphism is closed
to K because K is normal, thus containing all roots of a(x). So clearly then
any factorization of b(x) −α1 maps to an equivalent factorization of b(x) −αj
byσ; thus each component is irreducible if even one is irreducible.
Finally we simply take a(x) to have the highest possible degree and since this
requires each b(x) to have the smallest possible degree not all can have factors.
Since one b(x) −αi is irreducible, so are they all, and hence every irreducible
factor of f (x) over K[x] has the same degree – that of b(x). □
16 Transcendental Galois Groups. – True or False? Gal(k(x)/k) = 1. Hint: Consider substituting x
with 1/x.Example: False. Indeed Gal(k(x)/k) ∼= GL2(k). While the isomorphism is
not important we can show that at least all of GL2(k) is contained in the Galois
group.
Consider the map
Γ(p(x)) = p
(ax +b
cx +d
)
, ad −bc ⁄= 0,
where p(x) is any rational function in k(x). If a0 ∈ k then p(x) = a0 for any
entry of x so indeed Γ(p(x)) = a0 =p(x) proving Γ is a k-ﬁxing map. That Γ
is well-deﬁned follows because it is a an evaluation map. 2
2Formally it is a substitution homomorphism so nothing but bijectivity need be checked.
However as the map does not end in k, as we are substituting functions, it seem prudent to
verify all steps for completeness.

42 CHAPTER 2. FIELDS
Next we verify the homomorphism properties:
Γ(p(x) +q(x)) = Γ
( n∑
i=0
(pi +qi)xi
)
=
n∑
i=0
(pi +qi)
(ax +b
cx +d
)i
=
n∑
i=0
pi
(ax +b
cx +d
)i
+qi
(ax +b
cx +d
)i
= p
(ax +b
cx +d
)
+q
(ax +b
cx +d
)
= Γ( p(x)) + Γ(q(x)).
Now for multiplication:
Γ(p(x)q(x)) = Γ


n∑
i=0
m∑
j=0
piqjxi+j


=
n∑
i=0
m∑
j=0
piqj
(ax +b
cx +d
)i+j
=
n∑
i=0
m∑
j=0
pi
(ax +b
cx +d
)i
qj
(ax +b
cx +d
)j
=
n∑
i=0
pi
(ax +b
cx +d
)i m∑
j=0
qi
(ax +b
cx +d
)j
= Γ( p(x))Γ(q(x)).
Finally we realize that
Γ
(p(x)
q(x)
)
= Γ(p(x))
Γ(q(x))
so indeed it is suﬃcient to test homomorphism only on polynomials; therefore, Γ
is a k-homomorphism from k(x) to k(x) and as such must be a monomorphism
as well.
Finally that Γ is invertible follows from the assumption that ad ⁄=bc. This
makes the matrix invertible so that we have:
Γ−1(p(x)) = p
( −dx +b
cx −a
)
.
Clearly then
Γ(Γ−1(p(x))) = p
(
a −dx+b
cx−a +b
c −dx+b
cx−a +d
)
=p(x)
and likewise:
Γ−1(Γ(p(x))) = p
(
−dax+b
cx+d +b
cax+b
cx+d −a
)
=p(x).
So Γ is k(x) automorphism ﬁxing k. Hence Γ ∈Gal(k(x)/k). Moreover there is
a canonical bijection between Γ and the matrix
A(Γ) =
[a b
c d
]
, det (A(Γ)) ⁄= 0

Algebra – James Wilson 43
so indeed we have an embedding of GL2(k) in Gal(k(x)/k) so the Galois group
is not trivial. □
17 Field Extensions. Construct subﬁelds of C which are splitting ﬁelds Hint: Adjoin any real roots
ﬁrst, then ﬁnd the appropriate
primitive complex roots.
over Q for polynomials x3 − 1, x4 − 5x2 + 6, and x6 − 8. Find the degrees of
those ﬁelds as extensions over Q.
Example:
• The third roots of unity are 1,
ω =e2πi/3 = − 1
2 +i
√
3
2 ; ω2 =e4πi/3 = − 1
2 −i
√
3
2 .
For our extension we may drop the rational translations and coeﬃcients
to obtain Q(i
√
3) as a splitting ﬁeld of x3 − 1. In particular by dividing
byx − 1 we ﬁnd x2 +x + 1 is the irreducible component of x3 − 1 and so
the degree of the extension is 2.
• We begin by factoring our polynomial in C:
x4 − 5x2 + 6 = (x2 − 2)(x2 + 2) = (x −
√
2)(x +
√
2)(x −i
√
2)(x +i
√
2).
Thus the extension Q(
√
2,i ) is our desired splitting ﬁeld. This gives us a
basis for our splitting ﬁeld of
{1,
√
2,i,i
√
2}.
Therefore the degree of the extension is 4.
• When considering x6 − 8, we begin by considering the sixth roots of unity,
which are: {
±1,
(
± 1
2 ±i
√
3
2
)}
and the radius is
6√
8 =
√
2, so our splitting ﬁeld is Q(
√
2,i
√
3). As
x2 − 2 = irr(
√
2; Q) ⁄=irr(i
√
3; Q) = x3 + 3
it follows
{1,
√
2,i
√
3,i
√
6}
is a basis for the extension, and thus it has degree 4.
□
18 Normal Extensions. Which of the following extensions are normal? Hint: Try to verify if they are
splitting ﬁelds for some poly-
nomial.(a) Q(x)/Q;
(b) Q(√−5)/Q;
(c) Q(
7√
5)/Q;
(d) Q(
√
5,
7√
5)/Q(
7√
5);
(e) R(√−7)/R.
Example:

44 CHAPTER 2. FIELDS
(a) Let p(x) be an irreducible polynomial over Q. Then p(x) has all its roots
in C, but C ∩ Q(x) = Q so Q(x) has no roots of p(x), and thus vacuously
Q(x)/Q is normal. (Also recall its Galois group was trivial so normality it
for free.)
(b) The polynomial x2 + 5 has ±i
√
5 as a roots. It is enough now to claim
Q(i
√
5)/Q is the splitting ﬁeld of an irreducible polynomial so it is a normal
extension.
(c) Here note that x7 − 5 is irreducible by the rational roots theorem. Moreover
it has as a root,
7√
5. However it does not contain
ω =
7√
5(ei 2π
7 ),
as Q(
7√
5) ⊆ R and ω /∈ R since sin( 2π
7 ) ⁄= 0. Therefore we have an irre-
ducible polynomial with one root in the extension but yet does not split;
hence, the extension is not normal.
(d) Takex2 − 5; the roots are ±
√
5. Clearly any extension that contains one
contains the other. Therefore any extension that is generated by one is a
splitting ﬁeld for x2 − 5, and hence it is a normal extension.
(e) The polynomial x2 + 7 has the roots ±i
√
7 which again means the extension
is normal if it is the extension of one of these. Hence R(i
√
7)/R is normal.
In both these last two cases, the fact that the extension is of index 2 explains
why the extension is normal.
□
19 Extension Degrees. Let K/k be a splitting ﬁeld for a polynomialHint:
f (x) ∈k[x] of degree n. Show that [ K :k] divides n!.
Proof: The case for inseparable polynomials is unclear. We pretend these are
not important.
We know [K : k] = |Gal(K/k)|. Moreover, from our previous exercises we
know that the automorphisms in Gal(K/k) are uniquely determined by the per-
mutations they make on the roots of the irreducible polynomials that generate
the extension. Since K/k is splitting ﬁeld for f (x), it follows the roots a1,...,a n
off (x) determine K ∼=k(a1,...,a n). At best f (x) is irreducible at which point
the automorphisms may permute the n roots in what ever fashion they wish;
hence, Gal(K/k) = Sn, so [ K : k] = n!. But if f (x) is reducible, then the
automorphisms must only permute the roots within the irreducible factors in
which they are found. Therefore Gal(K/k) is a subgroup of Sn and so by the
theorem of Lagrange [ K :k] = Gal(K/k)|n!. □
20 Field Monomorphisms. – True or False? If K/k is a ﬁeld extensionHint: Consider a transcenden-
tal extension. then every k-monomorphism K →K is an automorphism.
Example: False. Consider the extension k(x)/k. If we deﬁne a map on the
basis elements 1,x,x 2,... by sending 1 to 1, x to x2, x2 to x4, and in general
xm to x2m, we determine conclusively a linear mapping f : k[x] → k[x] which
leavesk invariant. Moreover,
f (a(x)b(x)) = f (c(x)) = c(x2) = a(x2)b(x2).
Now if we rationalize k[x] we must ensure that f ′ : k(x) → k(x) remains well-
deﬁned, and we will thus have an monomorphism k(x) → k(x) which ﬁxes k
(recall ﬁelds have no ideals so the map is trivially monic.)

Algebra – James Wilson 45
We deﬁne f ′(a(x)/b(x)) = f (a(x))/f (b(x)). As b(x) ⁄= 0, it follows there
exists a coeﬃcient bi of b(x) which is non-zero. This element maps to b2i, thus
f (b(x)) ⁄= 0. Furthermore, given a(x)/b(x) = c(x)/d(x), it is equivalent to state
a(x)d(x) = b(x)c(x). Notice:
a(x2)d(x2) = f (a(x)d(x)) = f (b(x)c(x)) = b(x2)c(x2);
thus,f ′(a(x)/b(x)) = f (c(x)/d(x)) sof ′ is well-deﬁned, and thus ak-homomorphism
of k(x) to k(x).
Finally, notice that f (k[x]) = k[x2] so indeed f ′(k(x)) = k(x2) which is a
proper subset of k(x), and hence f ′ is not surjective so it is not an automor-
phism. □
21 Galois Groups. Determine the Galois groups fo the following extensions: Hint: Determine the degrees
of the extensions ﬁrst.
(a) Q(
√
2,
√
3)/Q;
(b) Q(
5√
3,e 2πi/5)/Q;
(c) Q(
3√
2,
√
2)/Q;
(d) Q(
3√
2,e 2πi/3)/Q.
(a) G =Gal(Q(
√
2,
√
3)/Q) = C2 ×C2.
Example: The polynomials x2 −2 andx2 −3 are monic minimal irreducible
polynomials for the roots
√
2 and
√
3 respectively. Hence the extension
Q(
√
2)/Q has degree 2 as does its Galois group since we have a separable
normal extension. Moreover, x2 − 3 is irreducible over Q(
√
2)/Q so the
extension Q(
√
2,
√
3)/Q(
√
2) has degree 2 as well so by the tower law we
have [Q(
√
2,
√
3) : Q] = 4 = |G|.
Any automorphism in the Galois group may permute
√
2 with −
√
2 and
likewise the pair ±
√
3. Thus we recognize every permutation has at most
order 2, so the group must be C2 ×C2. □
(b) G =Gal(Q(
5√
3,e 2πi/5)/Q) = Mr 20.
Mr 20 = ⟨a,b | a5 =b4 = 1,bab −1 =a2⟩.
Example: Since 5 is prime, e2πi/5 is a primitive 5th root of unity. Moreover,
5√
3 is a root of x5 − 3 so the extension is a splitting ﬁeld for x5 − 3. There
is only one real root as the derivative is nowhere negative so the graph is
increasing, thus having only one x-intercept. Therefore
p(x) = x5 − 3
x −
5√
3
is irreducible over R and so also over Q(
5√
3). Clearly p(x) has degree 4 so
we have ﬁnally that
[Q(
5√
3,e 2πi/5) : Q] = [ Q(
5√
3,e 2πi/5) : Q(
5√
3)][Q(
5√
3) : Q] = 20.
Since p(x) is not over Q it follows the roots are acted upon transitively.
Therefore we need a transitive subgroup of S5 of order 20. S5 cannot have
an element of order 10 – requires (12345)(67) cycle or greater.

46 CHAPTER 2. FIELDS
Let G be a group of order 20. By the third Sylow theorem we know there
exists a unique Sylow 5-subgroup, which must be isomorphic to C5. Let S4
be a Sylow 2-subgroup, it must have order 4. As (5 , 4) = 1 it follows C5 and
S4 intersect trivially. Moreover, C5S4 =G by the pigeon-hole-principle. As
C5 is the unique Sylow 5-subgroup it is normal in G. If we can establish
that G/C5 ∼=S4 we will be able to assert that G =C5 ⋊S4.
Suppose S4 = C4. Then there is precisely one C2 subgroup of S4 which
intersectsC5 trivially, so it produces an order 10 subgroup C5 <C 5C2 <G .
Moreover, if C5C2 ∼=C10, then any other Sylow 2-subgroup must intersect
C5C2 as there are only 10 elements left and if there is more than one C4
subgroup, these elements must all be their generators; thus their C2 sub-
groups are all the same. Finally if C5C2 ∼=D5 – the only other possibility,
then again as D5 require 5 involutions, all the C2 subgroups of the C4’s
intersectC5C2. Therefore, the only intermediate subgroup between C5 and
G is C5C2 so G/C5 ∼=C4 wheneverS4 ∼=C4.
Suppose S4 = C2 ×C2. Here the argument in simpler. If C5C2 contains
any two non-trivial elements of S4 then it contains all of S4 so it generates
G. This cannot be as we know C5 is normal so C5C2, which has order 10,
is a proper subgroup. Therefore each of the three proper subgroups of S4
generate their own order 10 subgroup, so in fact G/C5 has three proper
subgroups so it must be C2 ×C2.
Now we can sum up our result with the claim that the following diagram is
split exact:
1 /d47/d47C5
/d31 /d127 /d47/d47G /d47/d47 /d47/d47S4 /d47/d47 1.
Whence, there exists a homomorphism ϕ : S4 → Aut C5 = C4. This
determines the following table: (let ⟨a⟩ =C5 and b ∈S4)
ϕ :C4 /d47/d47 /d47/d47C4;
ϕ :C4 /d47/d47 /d47/d47C2
/d31 /d127 /d47/d47C4;
ϕ :C4 /d47/d47 /d47/d47 1/d31 /d127 /d47/d47C4;
ϕ :C2 ×C2 /d47/d47 /d47/d47C2
/d31 /d127 /d47/d47C4;
ϕ :C2 ×C2 /d47/d47 /d47/d47 1/d31 /d127 /d47/d47C4.
Which produces the following corresponding groups: 3
Mr 20 = ⟨a,b | a5 =b4 = 1,bab −1 =a2⟩
Q20 = ⟨a,b | a5 =b4 = 1,bab −1 =a−1⟩
Z20 = ⟨a,b | a5 =b4 = 1,bab −1 =a⟩
D20 = ⟨a,b | a5 =b2 = 1,bab −1 =a−1⟩
C2 ×C10 = ⟨a,b | a5 =b2 = 1,bab −1 =a⟩
3 The presentations all have the order of a and b together with a normal form relation;
thus they determine at most 20 elements, and by their construction at least 20, so they are
necessary and suﬃcient.

Algebra – James Wilson 47
We can observe that all but Mr 20 have Z10 as a subgroup. However we
know our Galois group lies in S5 so as there is no element of order 10 in S5
we must conclude the Galois group is Mr 20.4 □
(c) G =Gal(Q(
3√
2,
√
2)/Q) = C2
Example: Notice the irreducible polynomial x2 − 2 splits in our exten-
sion but the polynomial x3 − 2 only does so partially. Hence our given
extension is not normal. As such we only have the roots ±
√
2 and
3√
2 to
permute, but we cannot mix roots of diﬀerent irreducible factors. Hence we
only have permutations that transposed pm
√
2, so the Galois group is C2. □
(d) G =Gal(Q(
3√
2,
√
2,e 2πi/3)/Q) = C2 ×S3
Example: Since irr(
√
2; Q) = x2 − 2 and irr(
3√
2; Q(
√
2)) = x3 − 2 (ir-
reducibility follows from rational roots theorem) it follows our extension is
simply
Q(
√
2,
2√
2,ω )/Q(
√
2,
3√
2)/Q(
√
2)/Q
where we let ω =e2πi/3 which is a primitive third root of unity.
As such from the tower law we see the degrees of the extension are de-
termined by the irreducibles that cause them: so deg x2 − 2 = [ Q(
√
2) :
Q], deg x3 − 2 = [ Q(
√
2,
3√
2) : Q(
√
2)], and ﬁnally deg x2 + x + 1 =
[Q(
√
2,
3√
2,ω ) : Q(
√
2,
3√
2)] so our total extension degree is 12.
As this is the splitting ﬁeld for ( x2 − 2)(x3 − 2) we see that it is normal and
separable so its Galois group has order 12.
Since we have the intermediate ﬁeld Q(
√
2) of degree 2 it is normal, so
H = Gal(Q(
√
2,
3√
2,ω )/Q(
√
2)) ◁G, and moreover H has order 6. Also,
(ω,ω 2) is a permutation required by the transitive action on the roots of
x2 +x + 1 and it ﬁxed
√
2 so (ω,ω 2) ∈H. Also, the roots of x3 − 2 are
3√
2,
ω
3√
2 and ω2 3√
2 and are acted upon transitively so there must be a 3-cycle
σ = (
3√
2,ω
3√
2,ω 2 3√
2) in G. But as this ﬁxes
√
2 it is clear σ ∈ H also.
Hence visibly H is non-abelian so H ∼= S3. Finally we can rearrange the
tower to have an intermediate ﬁeld Q(
3√
2,ω ) which has degree 6 over Q as
it is the splitting ﬁeld for x2 − 3, and it also normal for the same reason.
Thus we have an order 2 subgroup K of G which does not intersect H and
that meets H atG, so we have the conditions for an internal direct product.
Hence from the isomorphism types of H and K we know G ∼=C2 ×S3. □
22 Finite Fields. Prove that the quotient ring R := F3[x]/(x2 + 1) is a ﬁeld Hint: Find the dimension of
the ﬁeld as an F3 vector space.of order 9. Exhibit an explicit generator for R×.
Example: Notice x2 + 1 is irreducible in F3 since
02 ≡ 0, 11, 22 ≡ 1 (mod 3) .
As such, x2 + 1 is the monic irreducible polynomial of its roots, and R is thus
an extension containing one of its roots i. Notice the degree of the extension
is 2 as the polynomial has degree 2. Hence, R = F3(i) and {1,i } is a basis for
R/F3. Visibly then R = F3 ⊕ F3 as a vector space, and so it has order 9.
4The title of Mr. 20 is clearly not a standard name for this group.

48 CHAPTER 2. FIELDS
Finally, the element 1 + i generates R× as
(1 +i)2 ≡ 2i, (1 +i)4 ≡ (2i)2 ≡ 2, (1 +i)8 ≡ 22 ≡ 1 (mod 3) .
Hence (1 +i) has order at least 8, in a group of degree 8, so it is a cyclic gener-
ator. □
23 pk-th roots in Finite Fields. – True or False? If F is a ﬁeld ofHint: Show the Frobenius ho-
momorphism is injective. characteristicp, α ∈F , then F contains at most one pkth root of α.
Proof: True. We must show that xpk
= ypk
implies x = y for all x,y ∈ F .
This will not ensure the existence of pkth roots, but it will determine them to
be unique upon existence. Notice this is a short application of the Freshman’s
Dream:
0 = (xpk
−ypk
) = (x −y)pk
.
This implies ( x −y)(x −y)pk−1 = 0, so x −y is a zero-divisor. In a ﬁeld this
requires x −y = 0, and so x =y. □
24 Normal Extensions ofC. – True or False? Every ﬁnite normal extensionHint: All such extensions are
algebraic. of C is normal over R.
Proof: True. Every ﬁnite extension of C is an algebraic extension. Yet C is
algebraically closed, so there are no polynomials with roots outside it, and so
every ﬁnite extension is a trivial extension. Thus every ﬁnite extension is C/C
and so as C/R is normal, so is every ﬁnite extension of C. □
25 Rational Function Fields. Let F be a ﬁeld, and F (x) be the ﬁeldHint: Construct a polynomial
that annihilates the given ra-
tional function.
of rational functions. Show F (x)/F ( x3
x+1 ) is a simple extension, determine its
degree, and irr(x;F ( x3
x+1 ).
Example: To construct a polynomial over F ( x3
x+1 ) with x as a root, we need to
ride ourselves of the fraction. Since x is to be our root we will consider inverting
our fraction as x+1
x3 . Here then we require the term x+1
x3 y in our polynomial p(y)
inF ( x3
x+1 )[y]. Since we want the minimal degree we will look no further and use
what we have to determine the remaining terms of the polynomial as:
p(y) = x + 1
x3 y3 −y − 1.
Since we want a monic minimal degree polynomial we will replace the polynomial
with
p(y) = y3 − x3
x + 1y − x3
x + 1.
By our construction this is monic and of minimal degree having x as a root,
so since x is not in F ( x3
x+1 ) it is irreducible, and indeed p(y) = irr(x;F ( x3
x+1 )).
Hence, the extension is of degree 3, and as it is ﬁnite it is simple. □
26 Normal Extensions. – True or False? If [K : k] = 2 then K/k isHint: Consider division by any
factor. normal.
Proof: True. Suppose [ K :k] = 2. Then there is a basis {1,a } for the exten-
sion, and so visibly a2 ∈ k. Thus x2 −a2 is an irreducible polynomial in k[x]
which splits in K, so the extension is normal. □
27 Separable Transitivity. For extensions F/K/k , if F/K and K/k areHint: Follow a root through
irreducible decompositions of
an irreducible over k, K, and
ﬁnally F .

Algebra – James Wilson 49
separable then F/k is separable.
Proof: Take an irreducible polynomial p(x) in k[x]. Over K[x] p(x) factors
into irreducible components. Since the extension K/k is separable no irreducible
component appears more than once, and thus each root appears in exactly one
of the irreducible components.
Now take any irreducible component and move to F [x]. Here the polynomial
may factor further into irreducible components. However, as F/K is separable,
once again each root appears exactly once and in exactly one of these second
generation irreducible components. Therefore together we see that every root
is a simple root over F . So F/k is separable. □
28 Counting Polynomials. Let p be prime. Then there are exactly Hint: Count the number of
roots for each irreducible.(qp −q)/p monic irreducible polynomials of degree p in Fq[x].
Proof: For every irreducible polynomial of degree p, the splitting ﬁeld is Fqp as
there is only one ﬁnite ﬁeld of this order. Now the extension is a splitting ﬁeld so
it is normal. Since p is prime there are no intermediate ﬁelds either. Now every
elementα in Fqp\Fq is irreducible and algebraic over Fq as the extension is ﬁnite.
With no intermediate ﬁelds it follows the irr(α; Fq) has degree p. Therefore of
the qp −q elements, each corresponds to an irreducible polynomial of degree p.
Since all ﬁnite ﬁeld extensions are separable, each irr(α; Fq) actually absorbs p
many elements so we have a total of qp−q
p irreducible polynomials over Fq. □
29 Intermediate Finite Fields. Let q = pn and d|n. Then Fq contains Hint: The Galois group of a
ﬁnite ﬁeld is cyclic.exactly one subﬁeld with pd elements. Conversely, if Fpd is a subﬁeld of Fpn
then d|n.
Proof: We know the Galois group of a ﬁnite ﬁeld extension over a ﬁnite ﬁeld is
cyclic. Moreover, if the degree of the extension is n, then the Galois group has
order n so it is the cyclic group Cn. Therefore from the Galois correspondence
we know there is one and only one subﬁeld of degree d over the prime subﬁeld,
for every d|n. □
30 Splitting Fields. If K/k is a ﬁnite normal separable ﬁeld extension, Hint: Notice the extension is
simple.then there exists an irreducible polynomial f ∈k[x] such that K is a splitting
ﬁeld for f overk.
Proof: Since the extension is ﬁnite and separable we know it is a simple exten-
sion. Thus K =k(α) for some α. Since the extension is ﬁnite it is algebraic so
irr(α;k) has a root in K. Yet K is normal so it follows all the roots of irr(α;k)
are in K so indeed irr(α;k) splits in K. And moreover K is a splitting ﬁeld of
irr(α;k). □
31 Simple Extensions. Every ﬁnite ﬁeld extension is simple. Hint: Consider an inseparable
extension.Example: Consider Fp(x,y )/Fp(xp,yp). Since it is the tower of extensions
Fp(x,y )/Fp(xp,y )/Fp(xp,yp) we see the degree is p2 – as there minimal monic
irreducible polynomials are zp −xp and zp −yp respectively. However the ex-
tension is not simple. We notice that for every a(x,y ) ∈ F [x,y ], we may use
the Freshman’s dream to get:
a(x,y )p =


m,n∑
i,j=0
ai,jxiyj


p
=
m,n∑
i,j=0
ap
i,jxipyjp ∈ Fp(xp,yp).
So rational functions a(x)
b(x)
p
are also in Fp(xp,yp). Hence no element in Fp(x,y )

50 CHAPTER 2. FIELDS
can have degree p2 over Fp(xp,yp) so the extension is not simple. □
32 Squares in Finite Fields. If F is a ﬁnite ﬁeld and a,b ∈ F are notHint: Consider the Galois
group of √a,
√
b. squares then ab is a square.
Proof: Suppose all three are not squares in F . Then the extension F (√a,
√
b)
(where √a is a solution of x2−a) contains
√
ab so it contains the three extensions
F (√a,
√
b)
/d115 /d115 /d115 /d115 /d115 /d115 /d115 /d115 /d115 /d115
/d75/d75/d75/d75/d75/d75/d75/d75/d75/d75
F (√a)
/d76/d76/d76/d76/d76/d76/d76/d76/d76/d76/d76 F (
√
ab) F (
√
b)
/d114/d114/d114/d114/d114/d114/d114/d114/d114/d114/d114
F
Now this may not be as the extension are all of degree 2 so it illustrates the
Galois extension of C2 ×C2. Since It is also to be a ﬁnite extension of a ﬁnite
ﬁeld, it must have a cyclic Galois group. Therefore √a =
√
b at which point aa
is clearly a square. □
33 Simple Transitivity. Let F/K/k with K/k ﬁnite separable and F/KHint:
simple. Then F/k is simple.
Proof: SinceK/k is ﬁnite and separable it is indeed a simple extensions. So let
K = k(α) for some α ∈ K. Moreover, as the extension is ﬁnite, α is algebraic
overk so αn ∈ k for some k. Now as F/K is simple let F = K(t). It follows
k(τ +α) ≤k(t,α ) = F . We wish to show F =k(t +α) so that we may conclude
the extension is simple. So consider
(u +α)n =
n∑
i=0
(n
i
)
un−iαi =
n−1∑
i=0
(n
i
)
un−iαi +αn.
Since αn ∈k it follows we have
u
(n−1∑
i=0
(n
i
)
un−iαi
)
α ∈k(τ +α).
□
34
35 There is no irreducible polynomial of degree 4 over Q with splitting ﬁeld
of degree 6.
Proof: Since Q has characteristic 0, all irreducible polynomials are separable;
thus, so is our degree 4 polynomial p(x). Moreover, the splitting ﬁeld will be
a normal extension and also ﬁnite, so we have a Galois extension allowing us
to conclude |Gal(p; Q)| = 6. As the Galois group acts transitively on the roots
of our polynomial we have to ﬁnd a transitive order 6 subgroup of S4. But the
best part is there are none (the only order 6 subgroups of S4 are Si
3, where i is
a ﬁxed point 1 ,..., 4.) So p(x) does not exist. □
37 Let ϕ be the Euler function and ε ∈ C be a primitive mth root of unity.
Prove that [ Q(ε +ε−1) : Q] = ϕ(m)/2.

Algebra – James Wilson 51
Proof: First of all note that the Euler- ϕ function is even for m >2. When
m = 2, the primitive 2th roots of unity is −1 which is in Q so the extension has
degree 1. Now consider m> 2.
Now notice x2 + (ε +ε−1)x − 1 is irreducible over Q(ε +ε−1) as it has as
a root ε. Therefore [ Q(ε) : Q(ε +ε−1)] = 2 so by the tower law [ Q(ε +ε−1) :
Q] = ϕ(m)/2.
It is interesting to furthermore note the irreducible polynomial for the ex-
tension Q(ε +ε−1)/Q is simply:
Υm(x) =
∏
a≤m/2,(a,m)=1
(x−(e2πi a
m +e2πi m−a
m ) =
∏
a≤m/2,(a,m)=1
(
x − 2 cos 2πa
m
)
.
And in fact Υ m(x) ∈ Z[x]. □
38 Let m> 1 be an odd integer. Show that Φ 2m(x) = Φm(−x).
Proof: Since m is odd, it follows ϕ(m) is even, and ϕ(2m) = ϕ(m).
Φm(−x) =
ϕ∏
i=1
(m)(−x −εi) = ( −1)ϕ(m)
ϕ∏
i=1
(m)(x +εi) =
ϕ∏
i=1
(2m)(x − (−ε)).
Notice ( −εi)2m − 1 = 0 for all primitive mth roots of unity. Since m is odd,
(−ε)d − 1 ⁄= 0 for any d|m. Therefore recalling x2m − 1 =∏
d|2m Φd(x) we now
see −εi are the roots of Φ 2m; wherefore, Φ m(−x) = Φ 2m(x). □
40 Show there exist f ∈k[x] where Gal(f ;k) acts transitively on f , but f is
reducible.
Example: The answer requires a repeated root. The simplest example is x2
over any ﬁeld k. Certainly the only root is 0 so any group acts transitively on
the roots – including our Gal(x2;k). Yet clearly x2 is reducible. □
41 Let K/k be a ﬁeld extension. If α1,...,α n ∈ K are algebraically
independent over k, and α ∈ k(α1,...,α n) −k, then α is transcendental over
k.
Proof: Let α = p(α1,...,αn)
q(α1,...,αn) where p(x1,...,x n),q (x1,...,x n) ∈ k[x1,...,x n]. Work of James, Dragos, and
DawnSupposeα is algebraic over k; say it is a root of a polynomial f (x) ∈k[x]. Then
f (α) = a0 +a1
p(α1,...,α n)
q(α1,...,α n) + · · · +am
p(α1,...,α n)m
q(α1,...,α n)m.
So we clear the denominators and take
g(x) = q(α1,...,α n)f (x).
However we may now take g(x) to be a polynomial in k(α)[x1,...,x n] in a
natural way as:
g(α)(x1,...,x n) = q(x1,...,x n)f (α)(x1,...,x n).
Notice then that g(α)(α1,...,α n) = 0. This means α1,...,α n is algebraically
dependent over k(α). This implies TrDeg (k(α1,...,α n)/k(α))<n .
Now by the Tower Law,
n = TrDeg (k(α1,...,α n) : k) = TrDeg (k(α1,...,α n) : k(α))TrDeg (k(α) : k)
= TrDeg (k(α1,...,α n)/k(α)).

52 CHAPTER 2. FIELDS
However, we now have a contradiction as the transcendence degree cannot be
both n and less than n. So α must be transcendental over k. □
42 Let k be a ﬁeld and x a transcendental element over k. Describe
Gal(k(x)/k).
Example: We know any two transcendental extensions are isomorphic ﬁelds.There is a no resolution on
a fully determined descrip-
tion of this extension’s Ga-
lois group. Certain condi-
tions on the ﬁelds, such as or-
der, may exclude maps that
here seem reasonable.
Therefore given any two such elements α,β we can construct an automorphism
sending α to β. □
44 Let G be a ﬁnite group of automorphism of a ﬁeld K with ﬁxed ﬁeld
k =KG. Show K/k is Galois and Gal(K/k) = G.
Proof: By Thm-2.7.3 we now [ K : k] = |G| so the extension is ﬁnite; fur-
thermore, if Gal(K/k) = G then by Thm-2.7.18 it follows K/k is normal and
separable, and thus Galois. All we must show now is that Gal(K/k) = G.
Certainly G ≤Gal(K/k), so we must now show these are all the elements.
It follows |G|[G∗ :k] = |Gal(K/k) but notice that G∗ =k so |G| = |Gal(K/k)
and since all is ﬁnite the pigeon-hole-principle applies to say G =Gal(K/k). □
45 Show if K/k is a splitting ﬁeld extension for f ∈ k[x], then [ K : k] ≤
(deg f)!.
Proof: We know from exercise 19 that [ K :k]|(deg f)! so it is immediate. □
46 Ifk is a ﬁeld, f ∈k[x], and K/k is a splitting ﬁeld then [ K :k] = (deg f)!
implies f is separable and irreducible.
Proof: Suppose f has a repeated root α. Then there exists a g(x) = k(α)[x]Thanks to Mike for the sep-
arability. and f (x) = (x −α)2g(x) – note we are guaranteed at least a factor of 2. Now it
follows that deg irr(α;k) ≤deg f anddeg g=deg f− 2. Thus using the result
from exercise 45 it is now clear that
[K :k] = [K :k(α)][k(α) : k] ≤ (deg f− 2)!(deg f) ⁄= (deg f)!
Whence f is must be separable to avoid contradictions.
We haven =deg f roots so as the Galois group is characterized completely
by its permutation on the roots it is clear Gal(K/k) is embedded in Sn. As we
know K/k is a separable normal extension it follows n! = [K/k] = |Gal(K/k)|
and so Gal(K/k) = Sn by the pigeon-hole principle. This means the group is
free to permute roots in any combination. However the group is also required to
permute roots only within the irreducible factors. Thus the entire polynomial
must be irreducible. □
47 Compute Gal(R/Q).
Example: Take any automorphism f : R → R. Such a map must be orderThanks to Hungerford and
Dragos preserving as: take x ∈ Q, x ≥ 0 then
f (x) = f (√x
2
) = (f (√x)2 > 0.
Therefore as the positive set is preserved, order is preserved. Now take any
r ∈ R. For all n ∈ N it follows there exists a rational q such thatq <r<q +1/n.
Hence f (q) = q <f (r)<f (q + 1/n) = q + 1/n. As n → ∞ we force f (r) = r.
□

Algebra – James Wilson 53
48 Compute Gal(Q(
√
2,
√
3,
√
5) : Q).
Example: Because 2, 3, and 5 are prime we conclude x2 − 2, x2 − 3 and
x2 − 5 are all irreducible over Q, Q(
√
2), and Q(
√
2,
√
3) respectively; monic;
and as they have degree 2 must be the corresponding polynomials irr(
√
2; Q),
irr(
√
3; Q(
√
2)) and irr(
√
5; Q(
√
2,
√
3)). As such each extension is of degree 2,
and so the entire extension is of degree 8. In fact we now say Q(
√
2,
√
3,
√
5) is
the splitting ﬁeld of f (x) = (x2 − 2)(x2 − 3)(x2 − 5). f (x) is clearly separable,
so the extension is Galois and hence |Gal(f ; Q)| = 8. Finally, the irreducible
factors are all of degree 2 so each automorphism is an involution. Therefore it
is the group C2 ×C2 ×C2.
□
49 Let K/k be a Galois extension, and L,M be intermediate ﬁelds. Denote
byLM the minimal subﬁeld of K containingL and M .
(i) Prove that (L ∩M )∗ = ⟨L∗,M ∗⟩.
(ii) Prove that (LM )∗ =L∗ ∩M ∗.
(iii) Prove that Gal(LM/L) ∼=Gal(L/(L ∩M )).
Proof: From the deﬁnition of a group join, we know
L∗ ∨M ∗ =
⋂
L∗,M ∗≤H
H.
So if we apply our dual ∗ we get:
(L∗ ∨M ∗)∗ =
⋃
L,M ≥H ∗
H ∗.
However we know H ∗ ≤ L ∩M whenever H ∗ ≤ L and M , as L ∩M is the
largest subﬁeld contained in both L andM , and indeed (L ∩M )∗ is such an H,
so L ∩M =⋃
L,M ≥H ∗H ∗, so in fact
(L∗ ∨M ∗) = ((L∗ ∨M ∗)∗)∗ = (L ∩M )∗.
Now consider (LM )∗. Given any σ ∈LM ∗ we know then σ ﬁxes L and M
so therefore σ ∈L∗ ∩M ∗. Moreover this tells us
(LM )∗ ≤L∗ ∩M ∗ ≤L∗,M ∗.
Applying the Galois correspondence we notice:
L,M ≤ (L∗ ∩M ∗)∗ ≤LM.
As (L∗ ∩M ∗)∗ is a ﬁeld containing both L and M , and now visibly contained
in the least such ﬁeld, it must be precisely the ﬁeld LM . Therefore ( LM )∗ =
(L∗ ∩M ∗).
Finally, let M/k be a normal extension. As such, M ∗ is normal in G =
Gal(K/k). Certainly then
L∗/(LM )∗ =L∗/(L∗ ∩M ∗) ∼=L∗M ∗/M∗ = (L ∩M )∗/M∗
by the second isomorphism theorem for groups. But notice L∗/(L∗ ∩M ∗) =
Gal(LM/L) andL∗M ∗/M∗ =Gal(M/L ∩M ); thus, Gal(LM/L) ∼=Gal(M/L ∩
M ). □

54 CHAPTER 2. FIELDS
Example: When L/k is not normal, it is possible that Gal(LM/L) not be
isomorphic to Gal(L/L ∩M ). For instance, take p(x) to be a polynomial over
Q whose Galois group in splitting ﬁeld K is isomorphic to A4. There must
correspond subﬁeld L and M which correspond to the subgroups L∗ =A3 and
M ∗ = ⟨(12)(34)⟩ respectively. Thus ( LM )∗ = L∗ ∩M ∗ = 1 and (L ∩M )∗ =
L∗ ∨M ∗ =A4. Notice then that
[LM :L] = [L∗ : (LM )∗] = 3, [L :L ∩M ] = [(L ∩M )∗ :L∗] = 4.
Since |Gal(LM/L)| = [LM : L] and |Gal(L/L ∩M )| = [L : L ∩M ] it follows
these groups cannot be isomorphic as they do not even have the same order. □
50 Letk be a subﬁeld of R andf ∈k[x] an irreducible cubic with discriminant
D. Then
(i) D> 0 if and only if f has three real roots;
(ii) D< 0 if and only if f has precisely one real root.
Proof: We take a result from analysis that states every cubic equation over R
has one real root. Therefore f has either three roots in R or only one, as complex
roots must come in conjugate pairs. When D = 0 it follows we have a repeated
root. This would imply the f is inseparable polynomial over a characteristic 0
ﬁeld, an impossibility. Therefore it suﬃces to show D >0 if and only if f has
only real roots and the second result will follow by the contrapositive in both
directions, together with D ⁄= 0 and the existence of only one or three real roots.
Leta1 ∈ R be the one real root, and a2+ib2 anda2−ib2 be the two conjugate
roots in C (possibly they are in R as well).
D = ( a1 − (a2 +ib2))2(a1 − (a2 −ib2))2((a2 +ib2) − (a2 −ib2))2
= ((( a1 −a2) −ib2))((a1 −a2) +ib2))(2ib2))2
= (( a1 −a2)2 +b2
2)2(2ib2)2
Now we see the discriminant is positive if and only if b2 = 0 which occurs if and
only if all roots are real. □
51 Let char k ⁄= 2 and f ∈ k[x] a cubic whose discriminant has a square
root in k, then f is either irreducible or splits in k.
Proof: If f has no multiple roots then by virtue of having a square root of
the discriminant in k, and char k ⁄= 2, we know Gal(f ;k) ≤ A3. Thus, the
Galois group is trivial implying f splits in k, or it is A3 implying there are no
roots of f ink (refer to Exercise-13, we have a transitive action on the roots of
a polynomial with no multiple roots so it is irreducible.)
Now for the cases when f has multiple roots. If f (x) = (x −α)3, then cer-
tainly it splits in k if and only if α ∈k, so when α /∈k it is irreducible. Suppose
f (x) = (x −α)2(x −β) in some splitting ﬁeld. If α ∈ k then it follows β ∈ k
as the only extension of a monomial is trivial. Now suppose α /∈k. If β is also
not in k then by the deﬁnition f is irreducible over k. Suppose instead β ∈k.
Then (x −α)2 is irreducible over k. If k has characteristic 0, then there are
no inseparable polynomials so α ∈k causing a contradiction. In the ﬁnal case,
k has characteristic greater than 2 by assumption. Since the characteristic is
greater than the degree of the polynomial, the polynomial cannot be insepara-
ble as the derivative test will not be 0. Therefore ( x −α)2 should be separable

Algebra – James Wilson 55
which it visibly is not. Thus this case cannot exist for any k with characteristic
not equal to 2. □
52 Letf be an irreducible separable quartic over a ﬁeld k andα be a root of
f . There is no ﬁeld properly between k andk(α) if and only if the Galois group
of f is A4 or S4.
Proof: Let K be splitting ﬁeld for f over k. As such the extension is Ga-
lois. Therefore the intermediate ﬁelds correspond precisely to intermediate sub-
groups. Since f is irreducible it follows [ k(α) : k] = 4. Also the automorphisms
need to act transitively on the 4 roots so it is in fact the case that the Galois
group is V,C 4,D 8,A 4 or S4.
The ﬁrst three are 2-groups. However we know from the ﬁrst Sylow theorem
that every 2-subgroup lies inside a 4-subgroup of any 8-group. Thus none of
these groups of a subgroup of index 4 with no intermediate group. Therefore
the corresponding ﬁeld extension with these Galois groups will have no such
case where [k(α) : k] = 4 and there are no intermediate ﬁelds.
This leaves S4 andA4. All we need to do is conﬁrm they have subgroups of
index 4 with no intermediate subgroups. This follows empirically by noticing
S3 inS4 andA3 inA4. If S3 is contained in an intermediate subgroup, this sub-
group must have order 12. However there is only one order 12 subgroup of S4
which is A4. Moreover, S3 is not in A4 asA4 does not contain any subgroup of
order 6. This last statement in fact also explains why there are no intermediate
subgroups between A3 and A4. Therefore both S4 and A4 are candidates for
such a situation. □
53 Every element of a ﬁnite ﬁeld can be expressed as a sum of two squares.
Proof:
□
54 Determine the Galois group of x3 + 11 over Q, determine all subﬁelds of
its splitting ﬁeld, and decide which are normal over Q. Describe the subﬁelds
by their generators.
Proof: The polynomial splits as
(x −
3√
11)(x2 −
3√
11x +
3√
112).
Therefore letting α = 1
2 −i
√
3
2 we have α and −α2 as roots of x2 −x + 1. So we
have a splitting extension of Q(
3√
11,α )/Q. The degree is equal to
[Q(
3√
11,α ) : Q(
3√
11)][Q(
3√
11) : Q] = 2 · 3 = 6
as x3 + 11 is irreducible over Q and the roots of x2 −x + 1 are complex so it is
irreducible over Q(
3√
11).
Since x3 + 11 is irreducible, its Galois group is a transitive group on all
irreducible components – here there is only one (there can only ever be one
with any irreducible degree 3 polynomial: you cannot split only three elements
into non-trivial imprimitivity blocks.) The only group of order 6 that acts
transitively on 3 elements is S3 so the Galois group is S3.

56 CHAPTER 2. FIELDS
The intermediate ﬁelds are exhibited as
Q(
3√
11,α )
/d6 /d6 /d6 /d6 /d6 /d6 /d6 /d6 /d6 /d6 /d6 /d6 /d6 /d6 /d6 /d6 /d6
/d82/d82/d82/d82/d82/d82/d82/d82/d82/d82/d82/d82/d82
/d89/d89/d89/d89/d89/d89/d89/d89/d89/d89/d89/d89/d89/d89/d89/d89/d89/d89/d89/d89/d89/d89/d89/d89/d89/d89/d89/d89/d89/d89/d89/d89
Q(
3√
11) Q(α
3√
11)
/d120 /d120 /d120 /d120 /d120 /d120 /d120 /d120 /d120 /d120 /d120 /d120 /d120 /d120 /d120 /d120 /d120 /d120 /d120 /d120 /d120 /d120
Q(−α2 3√
11)
/d107 /d107 /d107 /d107 /d107 /d107 /d107 /d107 /d107 /d107 /d107 /d107 /d107 /d107 /d107 /d107 /d107 /d107 /d107 /d107 /d107 /d107 /d107 /d107 /d107 /d107 /d107 /d107 /d107 /d107 /d107 /d107 /d107 /d107 /d107 /d107 /d107 /d107 /d107
Q(α)
/d75/d75/d75/d75/d75/d75/d75/d75/d75/d75/d75
Q
Certainly every subﬁeld is normal in Q(
3√
11,α ) as it is a splitting ﬁeld – more-
over it corresponds to the trivial group which is normal in all subgroups. Finally
we should expect to observe the Q(α)/Q is normal. This is true in two ways:
ﬁrst it is the splitting ﬁeld for x2 −x + 1, and second it is of degree 2. We also
observe the remaining intermediate ﬁelds are not normal as in each case, the
polynomial x3 + 11 does not split in them even though each contains a root of
x3 + 11.
To be certain of our construction we must verify the automorphism exist
that correspond to this ﬁeld extension. Deﬁne σ(
3√
11) = −α2 3√
11 and leaving
α invariant. By the fact that both are roots of the same monic minimal degree
irreducible polynomial, we know there exists a ﬁeld monomorphism σ and as
it lies inside a normal extension we may extend this to Q-automorphism of
Q(
3√
11,α ). Notice then
σ(α
3√
11) = σ(α) −α2 3√
11 = −α3 3√
11 =
3√
11,
σ(α2 3√
11) = −α4 3√
11 = α
3√
11,
so that in fact σ = (
3√
11, −α2 3√
11,α
3√
11). Therefore σ has order 3 – it is A3 –
and it ﬁxes Q(α) as predicted.
In similar fashion,τ (
3√
11) =
3√
11 andτ (α) = −α2 again produces a monomor-
phism of
Q(α,
3√
11)/Q(
3√
11) → Q(−α2,
3√
11)
by the fact that α and −α2 share the same monic minimal degree irreducible
polynomial. Clearly this is an automorphism of Q(α,
3√
11). Furthermore,
τ = (α
3√
11, −α2 3√
11) so τ has order 2, and ﬁxes Q(
3√
11) so the correspon-
dence is veriﬁed. □
56 Find all subﬁelds of the splitting ﬁeld for x3 − 7 over Q. Determine its
Galois group, and which subﬁelds are normal.
Proof: The polynomial splits as
(x −
3√
7)(x2 +
3√
7x +
3√
72).
Therefore letting α = − 1
2 −i
√
3
2 then α and α2 are the roots of x2 −x + 1;
whence, we have a splitting extension of Q(
3√
7,α )/Q. The degree is equal to
[Q(
3√
7,α ) : Q(
3√
7)][Q(
3√
7) : Q] = 2 · 3 = 6
as x3 + 7 is irreducible over Q and the roots of x2 −x + 1 are complex so it is
irreducible over Q(
3√
7).

Algebra – James Wilson 57
Sincex3 +7 is irreducible, its Galois group is a transitive group on 3 elements
with order 6 – it is S3.
The intermediate ﬁelds are exhibited as
Q(
3√
7,α )
/d7 /d7 /d7 /d7 /d7 /d7 /d7 /d7 /d7 /d7 /d7 /d7 /d7 /d7 /d7 /d7 /d7
/d81/d81/d81/d81/d81/d81/d81/d81/d81/d81/d81/d81/d81
/d88/d88/d88/d88/d88/d88/d88/d88/d88/d88/d88/d88/d88/d88/d88/d88/d88/d88/d88/d88/d88/d88/d88/d88/d88/d88/d88/d88/d88/d88/d88
Q(
3√
7) Q(α
3√
7)
/d121 /d121 /d121 /d121 /d121 /d121 /d121 /d121 /d121 /d121 /d121 /d121 /d121 /d121 /d121 /d121 /d121 /d121 /d121 /d121 /d121
Q(α2 3√
7)
/d108 /d108 /d108 /d108 /d108 /d108 /d108 /d108 /d108 /d108 /d108 /d108 /d108 /d108 /d108 /d108 /d108 /d108 /d108 /d108 /d108 /d108 /d108 /d108 /d108 /d108 /d108 /d108 /d108 /d108 /d108 /d108 /d108 /d108 /d108 /d108 /d108
Q(α)
/d74/d74/d74/d74/d74/d74/d74/d74/d74/d74/d74
Q
Certainly every subﬁeld is normal in Q(
3√
7,α ) as it is a splitting ﬁeld – moreover
it corresponds to the trivial group which is normal in all subgroups. Finally we
should expect to observe the Q(α)/Q is normal. This is true in two ways: ﬁrst
it is the splitting ﬁeld for x2 +x + 1, and second it is of degree 2. We also
observe the remaining intermediate ﬁelds are not normal as in each case, the
polynomial x3 + 7 does not split in them even though each contains a root of
x3 + 7.
To be certain of our construction we must verify the automorphism exist
that correspond to this ﬁeld extension. Deﬁne σ(
3√
7) = α
3√
7 and leaving α
invariant. By the fact that both are roots of the same monic minimal degree
irreducible polynomial, we know there exists a ﬁeld monomorphism σ and as
it lies inside a normal extension we may extend this to Q-automorphism of
Q(
3√
7,α ). Notice then
σ(α
3√
7) = σ(α)α
3√
7 = α2 3√
7
so that in fact σ = (
3√
7,α
3√
7,α 2 3√
7). Therefore σ has order 3 – it is A3 – and
it ﬁxes Q(α) as predicted.
In similar fashion, τ (
3√
7) =
3√
7 and τ (α) = α2 again produces a monomor-
phism of
Q(α, [3]7)/Q(
3√
7) → Q(α2,
3√
7)
by the fact that α and α2 share the same monic minimal degree irreducible
polynomial. Clearly this is an automorphism of Q(α,
3√
7). Furthermore, τ =
(α
3√
7,α 2 3√
7) so τ has order 2, and ﬁxes Q(
3√
7) so the correspondence is veri-
ﬁed. □
57 Let K be a splitting ﬁeld for x4 + 6x2 + 5 over Q. Find all subﬁelds of
K.
Proof: Notice
x4 + 6x2 + 5 = (x2 + 1)(x2 + 5) = (x −i)(x +i)(x −i
√
5)(x +i
√
5),
and, irr(i; Q) = x2 + 1 and irr(i
√
5; Q) = x2 + 5. Thus we have know our
splitting ﬁeld to be Q(i,
√
5)/Q. Moreover, its degree is 4 as deg irr(
√
5; Q) = 2
and as all the roots of x2 + 1 are complex, it is irreducible over Q(
√
5) we obtain
the tower of extensions:
[Q(i,
√
5) : Q] = [ Q(i,
√
5) : Q(
√
5)][Q(
√
5) : Q] = 4.

58 CHAPTER 2. FIELDS
Since the irreducible factors each contain only two of the roots it follows the
Galois group lies in S4 but it not transitive on the four elements. There is only
one such family of subgroups in S4, the Klein-4-groups of the form:
K 1
4 = {(1), (1 2), (3 4), (1 2)(3 4) }.
So this is our Galois group:
G = {(i), (i −i), (i
√
5 −i
√
5), (i −i)(i
√
5 −i
√
5)}.
Note the automorphisms exist and are well-deﬁned as they are clearly the ex-
tension of the Q-monomorphisms i → −i etc. which have the same irreducible
polynomial so they are justiﬁed.
Hence the subﬁelds of K correspond to this lattice. Having the automor-
phisms in hand we can compute the subﬁelds as
Q(i,
√
5)
/d110 /d110 /d110 /d110 /d110 /d110 /d110 /d110 /d110 /d110 /d110 /d110 /d110
/d81/d81/d81/d81/d81/d81/d81/d81/d81/d81/d81/d81/d81
Q(i)
/d80/d80/d80/d80/d80/d80/d80/d80/d80/d80/d80/d80/d80/d80/d80/d80 Q(
√
5) Q(i
√
5)
/d109 /d109 /d109 /d109 /d109 /d109 /d109 /d109 /d109 /d109 /d109 /d109 /d109 /d109 /d109
Q
In particular, Q(i) is the ﬁx ﬁeld of σ(i) = i and σ(
√
5) = −
√
5, which is to
sayσ = (i
√
5, −i
√
5); Q(
√
5) is ﬁxed in τ = (i, −i); and ﬁnally Q(i
√
5) is ﬁxed
by (i −i)(i
√
5 −i
√
5), as i
√
5 → −i
√
5 →i
√
5. All are normal as Q(i) is the
splitting ﬁeld of x2 + 1, Q(
√
5) of x2 − 5 and Q(i
√
5) that of x2 + 5. □
58 Let K be a splitting ﬁeld for x4 − 3 over Q(i). Find the Galois group of
K over Q(i).
Proof:
x4 − 3 = (x2 −
√
3)(x2 +
√
3) = (x −
4√
3)(x +
4√
3)(x −i
4√
3)(x +i
4√
3).
Therefore Q(
4√
3,i )/Q(i) is a splitting ﬁeld. Moreover, as
4√
3 /∈ Q(i) it follows
x4 − 3 is irreducible over Q(i). Moreover, the irreducible factors are not over
Q(i) so there is only one irreducible component and thus the Galois group acts
transitively on all four roots.
The degree of the extension is 4 as the irr(
4√
3; Q(i)) = x4 − 3. Therefore
the Galois group is V or C4. There is however only one intermediate ﬁeld:
Q(
√
3,i )/Q(i). So it must be C4. □
59 Let ε ∈ C be a primitive 7th root of unity. Determine the minimal
polynomial of ε, the structure of the Galois group, and the subﬁelds.
Proof: We know xp−1
x−1 is irreducible over Q and certainly this is nothing moreWork with Dawn.
than Φ 7 so it has ε as a root. Now the Galois group of a Cyclotomic extension
is cyclic (mostly by design) so it must be the cyclic group C6. Therefore we
expect to ﬁnd two proper intermediate ﬁelds.
To formalize the Galois group we can take σk as a Q-automorphism of
Q(ε)/Q with e2πi/7 ↦→ e2πik/7 and k ∈ Z×
7 . The automorphism is σ1 is unit
and σ3 is a generator. From here we identify the intermediate ﬁelds as ⟨σ2⟩∗
and ⟨σ6⟩∗. □

Algebra – James Wilson 59
60 Let K = Q(i,e 2πi/3), where i = √−1 in C. Find [ K : Q] and determine
Gal(K/Q).
Example: The polynomial x3−1
x−1 has roots − 1
2 ±i
√
32. Certainly
√
3 /∈ Q(i) so
Φ3(x) = x3−1
x−1 is irreducible over Q(i). Hence [ K : Q] = [K : Q(i)][Q(i) : Q] =
2 · 2 = 4. Moreover, the extension is no visibly a splitting ﬁeld of ( x2 + 1)Φ3(x)
so it is normal, and as Q has characteristic 0 also separable; therefore, the
extension is Galois. Moreover, the Galois group must act transitively on the
irreducible factors, which are x2 + 1 and Φ 3(x) respectively. As both of these
have only two roots we see that no automorphism in Gal(K/Q) can have order
greater than 2 (they are all transpositions when restricted to the roots of the
irreducible factors). As there are only two groups of order 4, we must conclude
the Galois group of the extension is C2 ×C2 as C4 has elements of order 4. In
particular
Gal(K/Q) = ⟨(i, −i), (e2πi/3,e 4πi/3)⟩.
□
68 In a ﬁeld of characteristic p, there is one pm-th root of unity.
Proof: By the Freshman’s dream we know
xpm
− 1 = (x − 1)pm
.
Hence this polynomial has only one root, so there is at most one pm-th root of
unity. Each certainly has at least one root of unity – simply 1. Thus there is
precisely one pm-th root of unity. □
72 If F is a ﬁnite ﬁeld and f ∈F [x] is irreducible then f ′(x) ⁄= 0.
Proof: Let F have characteristic p > 0, which it must have as it is a ﬁnite
ﬁeld.
Suppose f ′(x) = 0. Then there exists some g(x) ∈ F [x] such that f (x) =
g(xp) (this way the non-zero coeﬃcients are annihilated.) Now F is a ﬁnite
ﬁeld so the Frobenius map a ↦→ ap is an automorphism of F . Therefore every
element has a p-th root in F – we will denote such a root as p√a. In this way
we see:
g(xp) = a0 +a1xp + · · · +anxpn
= ( p√a0)p + ( p√a1)pxp + · · · + ( p√an)pxpn
= ( p√a0 + p√a1x + · · · + p√anxn)p
= ( f2(x))p.
Visibly f (x) is reducible as p > 1. As all other polynomials have non-zero
derivatives it follows any irreducible polynomial over F has non-zero derivative.
□
77 Show there is a Galois extension of F125 with Galois group C6.
Example: Notice 125 = 5 3 so we begin by acknowledging F518 exists as it is the
splitting ﬁeld of x518
−x over F5. Now as 3 |18 we have F125 ≤ F3,814,697,265,625.
Moreover, the degree of [ F125 : F5] = 3 so [ F3,814,697,265,625 : F125] = 6. As the
Galois group of F3,814,697,265,625/F5 is C18, the subgroups are all cyclic, so the
Galois group of F3,814,697,265,625/F125 is C6. □

60 CHAPTER 2. FIELDS
78 Every Galois extension of C is Galois over R.
Proof: Every Galois extension is ﬁnite, so it is algebraic. However C is al-
gebraically closed so there are only trivial Galois extensions. Therefore the
question is equivalent to asking if C is a Galois extension of R. Certainly so as
it has degree 2 which is both ﬁnite and also indicates normal, and it is over a
ﬁeld of characteristic 0 so it is separable. □
80 Let k be a subﬁeld of an algebraically closed ﬁeld K such that the
transcendence degree is ﬁnite. Prove that if ϕ :K →K is a k-monomorphism,
then ϕ is an automorphism of K.
Proof: Let T = {a1,...,a n} be a transcendence basis of K. Since ϕ is a
monomorphism it follows ϕ(T ) is a set with cardinality n. Moreover, if ϕ(T )
is algebraically dependent, then there exists some p(x1,...,x n) ∈k[x1,...,x n]
such thatp(ϕ(a1),...,ϕ (an)) = 0. Since ϕ|k(T ) is bijective, ﬁxing k, we see that
0 = ϕ−1(0) = ϕ−1(p(ϕ(a1,...,ϕ (an)) = p(a1,...,a n).
This contradicts the assumption that T is algebraically independent. Whence
we now see ϕ(T ) is as well. Since it has the same size as the transcendence
degree it follows ϕ(T ) is a transcendence basis for K. Therefore indeed we now
see that ϕ is an automorphism of k(T ) – the purely transcendental extension of
k in K. Now we look to the algebraic material.
We know that any k(T )-monomorphism of k(T )(α) lies in k(T )(β) where
α and β are roots of the same irreducible. Therefore ϕ|k(T )(A) is an automor-
phism of k(T )(A) for any set A of all roots of any given irreducible. Since K is
algebraically closed, we know K/k(T ) is precisely the extension of adjoining all
roots, so in fact ϕ is an automorphism of all of K. □
83 Letf ∈ Fp[x] such that f ′ = 0, then any splitting ﬁeld for f is separable.
Proof: Letα be any element in the splitting ﬁeld and take g(x) to be irr(α;k).
If the extension is to be inseparable then we may suppose that g(x) is an ex-
ample of an inseparable polynomial that makes it so. However, for g(x) to be
inseparable it must have a 0 derivative. Whence g(x) is irreducible if and only
at least one coeﬃcient has no p-th root in k. However k is a ﬁnite ﬁeld of char-
acteristicp. Therefore the Frobenius map is an automorphism, so every element
has a p-th root in k. This leads to a contradiction: either g(x) is reducible –
impossible by the choice of g(x), or it is separable. So it must be separable, and
now as every minimal polynomial is separable, the extension is separable. □
84 A ﬁeld of order 243 contains exactly one proper subﬁeld.
Proof: First factor 243 into 3 5. Since the existence of intermediate ﬁelds is
purely a number theory game we quickly notice since 5 is prime, the only divi-
sors are 1 and 5, so the only subﬁeld is F3 and in fact F243 has only one proper
subﬁeld. □
85 Give an example of a ﬁnite extension K/Fq in which two intermediate
ﬁelds L and M are incomparable.
Example: The smallest such example comes from extending Fq to Fq6. Be-
cause of the extension has Galois group C6 (simply because the degree of the
extension is 6, and the Galois group of a ﬁnite ﬁeld extension of a ﬁnite ﬁeld
must be cyclic.) The group C6 has two incomparable subgroups – one of order
2, another of order 3 – so there is precisely the same correspondence in the

Algebra – James Wilson 61
subﬁelds. □
86 Prove in a ﬁnite extension of a ﬁnite ﬁeld every intermediate ﬁeld is stable
(every automorphism of the intermediate ﬁeld maps back into the subﬁeld.)
Proof: The Galois group of any such extension must be cyclic. As such every
subgroup is normal. Normal subgroups imply normal intermediate ﬁelds. If an
intermediate ﬁeld extension is normal then it stable. □
88 Show the ﬁeld extension Q(x)/Q(x6) is not a Galois extension.
Example: Consider the polynomial y6 −x6 ∈ Q(x6)[y]. Certainly x is a root,
and furthermore we can factor y6 −x6 as
(y −x)(y +x)(y2 −yx +x2)(y2 +yx +x2).
Since we are over Q we can apply the quadratic formula to solve for the remain-
ing factors:
y = ±x ±
√
−3x2
2 .
Now we notice that the remaining roots are complex so their monomials are not
over Q(x6). Now by inspection:
(y −x)(y +x) = y2 −x2 /∈ Q(x6)
(y −x)(y2 +yx +x2) = y3 −x3 /∈ Q(x6)
(y −x)(y2 −yx +x2) = y3 − 2y2x + 2yx2 −x3 /∈ Q(x6)
(y +x)(y2 +yx +x2) = y3 + 2y2x + 2yx2 +x3 /∈ Q(x6)
(y +x)(y2 −yx +x2) = y3 +x3 /∈ Q(x6)
(y2 +yx +x2)(y2 −yx +x2) = y4 +y2x2 +x4 /∈ Q(x6).
Therefore y6 −x6 is irreducible as none of its proper factors is over Q(x6) and
none of the roots are in Q(x6). However this illustrates that the extension is
not Galois as it does not contain any of the complex roots but it does contain
some roots, so the extension is not normal, hence, not Galois. □
89 Let K/k be a ﬁnite ﬁeld extension and L,M be intermediate ﬁelds such
that L ∩M =k. Prove [ LM :k] ≤ [L :k][M :k] and show by example that a
strict inequality is possible.
Proof: Notice LM = L(M ); whence, [ LM : k] = [ LM : L][L : k]. Now
extend a basis from the linearly independent set {1} for the vector space LM
overL. This basis A = {1 = a1,a 2,...,a m} if ﬁnite since we lie in a ﬁnite ﬁeld
extension. Moreover, if any two basis vectors lie in L then they are linearly
dependent so in fact all A ⊂ M −L ∪ {1} since the only element from L is
the vector 1. Therefore [ LM : L] ≤ [M : L ∩M ] Now recall L ∩M = k, so
[LM :L] ≤ [M :L ∩M ] = [M :k]. Therefore we now observe that:
[LM :k] ≤ [M :k][L :k].
□
Example: Consider the splitting ﬁeld in C of x3 − 7 over Q. We have already

62 CHAPTER 2. FIELDS
established that this possess the intermediate ﬁelds:
Q(
3√
7,α )
/d7 /d7 /d7 /d7 /d7 /d7 /d7 /d7 /d7 /d7 /d7 /d7 /d7 /d7 /d7 /d7 /d7
/d81/d81/d81/d81/d81/d81/d81/d81/d81/d81/d81/d81/d81
/d88/d88/d88/d88/d88/d88/d88/d88/d88/d88/d88/d88/d88/d88/d88/d88/d88/d88/d88/d88/d88/d88/d88/d88/d88/d88/d88/d88/d88/d88/d88
Q(
3√
7) Q(α
3√
7)
/d121 /d121 /d121 /d121 /d121 /d121 /d121 /d121 /d121 /d121 /d121 /d121 /d121 /d121 /d121 /d121 /d121 /d121 /d121 /d121 /d121
Q(α2 3√
7)
/d108 /d108 /d108 /d108 /d108 /d108 /d108 /d108 /d108 /d108 /d108 /d108 /d108 /d108 /d108 /d108 /d108 /d108 /d108 /d108 /d108 /d108 /d108 /d108 /d108 /d108 /d108 /d108 /d108 /d108 /d108 /d108 /d108 /d108 /d108 /d108 /d108
Q(α)
/d74/d74/d74/d74/d74/d74/d74/d74/d74/d74/d74
Q
Notice then the intermediate ﬁelds L = Q(
3√
7) and M = Q(α
3√
7) intersect at
Q and join at Q(
3√
7,α ). Therefore
6 = [LM : Q] ≤ 9 = [L : Q][M : Q].
□
91 Letk be a ﬁeld, p(x) an irreducible polynomial in k[x] of degree n, and let
K be a Galois extension of k containing a root α of p(x). Let G =Gal(K/k),
and Gα be the set of all σ ∈G with σ(α) = α.
(a) Show that Gα has index n in G.
(b) Show that if Gα is normal in G, then p(x) splits in the ﬁxed ﬁeld of Gα.
Proof: To begin with, given any two σ,τ ∈ Gα it follows σ(α) = α and
τ (α) = α so στ (α) = σ(α) = α so στ ∈ Gα. Naturally 1( α) = α so 1 ∈ Gα.
Finally α = σ−1(σ(α)) = σ−1(α) by the deﬁnition of functional inverses, so
σ−1 ∈Gα and so Γ α is a subgroup of G.
Of importance is the fact the K is a Galois extension over k. Thus it is
normal and ﬁnite, so G is ﬁnite and p(x) splits in K as it contains one root in
K. Therefore G contains the Galois group of p(x).
Notice p(x) has degree n and is irreducible so [ k(α) : k] = n. As Gα ﬁxes
α and all of k it is certainly contained in k(α)∗. Now we must show this is
suﬃcient. Given any σ which ﬁxed k(α) it follows σ(α) = α so indeed σ ∈Gα.
Therefore Gα = k(α)∗. As such the by the Galois correspondence we know
[G :Gα] = [k(α) : k] = n.
Now suppose Gα is normal in G. Then as Gα =k(α)∗ and the extension is
Galois it follows ∗ is invertible so G∗
α = k(α), so k(α) is normal over k. As it
contains one root of p(x) it must contain all roots, so p(x) splits in k(α). □
92 Let k(α)/k be a ﬁeld extension obtained by adjoining a root α of an
irreducible separable polynomial f ∈ k[x]. Then there exists an intermediate
ﬁeld k < F < k(α) if and only if the Galois group Gal(f ;k) is imprimitive. If
the group is imprimitive then the subﬁeld F can be chosen so that [ F : k] is
equal to the number of imprimitivity blocks.
Proof: If the Galois group is primitive then it has maximal stabilizer of α.
HoweverGα determines the ﬁeld k(α) (see 91) that is now minimal over k, so
there is no intermediate ﬁeld. Whence in the contrapositive if an intermediate
ﬁeld exists then G is imprimitive.

Algebra – James Wilson 63
Now suppose G acts imprimitively on the roots of f . Then there is a non-
trivial block decomposition of the roots, one of which contains α, call this block
B. Every element that stabilizes α must also act inside the block of B. Fur-
thermore, G acts transitively inside B so there exists and element g ∈ G such
that gα = β for some distinct β ∈ B. Therefore GB – the elements that act
inside of B (perhaps stabilize B is the proper term, only they are not actually
ﬁxing elements of B) – is a proper parent group of Gα. As such it corresponds
to and intermediate ﬁeld k < G∗
B < G∗
α. Moreover we now see that the index
[G : GB] is the number of imprimitivity blocks so we have the required ﬁeld
whose extension degree is the number of imprimitivity blocks. □

64 CHAPTER 2. FIELDS

Chapter 3
Modules
1 Noetherian/Artinian Rings. . . . . . . . . . . . . . . 68
2 D.C.C. submodules and quotients. . . . . . . . . . . 69
3 Modules over artinian Rings. . . . . . . . . . . . . . 69
4 Sum decomposition of A.C.C./D.C.C. . . . . . . . . 69
5 Module Bases. . . . . . . . . . . . . . . . . . . . . . . 70
6 T/F Uniqueness of Module Decomposition. . . . . . . . . 71
7 Maschke’s Theorem. . . . . . . . . . . . . . . . . . . 71
8 T/F Module Annihilators. . . . . . . . . . . . . . . . . . . 71
9 Divisor Chains. . . . . . . . . . . . . . . . . . . . . . 72
10 T/F Composition Series . . . . . . . . . . . . . . . . . . . 73
11 T/F Free Submodules . . . . . . . . . . . . . . . . . . . . 73
12 T/F Free Submodules . . . . . . . . . . . . . . . . . . . . 73
13 T/F Free PID Modules . . . . . . . . . . . . . . . . . . . 73
14 T/F Free Inheritance . . . . . . . . . . . . . . . . . . . . . 74
15 T/F PID Quotients . . . . . . . . . . . . . . . . . . . . . 74
16 T/F PID subrings . . . . . . . . . . . . . . . . . . . . . . 74
17 T/F Polynomials over PIDs . . . . . . . . . . . . . . . . . 74
18 T/F Polynomials over Artinian Rings . . . . . . . . . . . 74
19 T/F Torsion Free vs. Free . . . . . . . . . . . . . . . . . . 74
20 Hom over PIDs . . . . . . . . . . . . . . . . . . . . . 75
21 Pure Submodules . . . . . . . . . . . . . . . . . . . . 76
22 Invariant Factors . . . . . . . . . . . . . . . . . . . . 76
23 Smith Normal From . . . . . . . . . . . . . . . . . . 78
24 T/F Invariant Factors . . . . . . . . . . . . . . . . . . . . 78
25 T/F Left Regular Modules . . . . . . . . . . . . . . . . . 79
26 T/F Matrix Equivalence . . . . . . . . . . . . . . . . . . . 79
27 Invariant Factors . . . . . . . . . . . . . . . . . . . . 80
28 Primary Decomposition . . . . . . . . . . . . . . . . 80
29 T/F Endomorphisms over PIDs . . . . . . . . . . . . . . . 80
30 T/F Endomorphisms over PIDs . . . . . . . . . . . . . . . 80
31 T/F Torsion Free vs. Free . . . . . . . . . . . . . . . . . . 80
32 T/F Rank Ordering . . . . . . . . . . . . . . . . . . . . . 81
33 T/F Free Quotients . . . . . . . . . . . . . . . . . . . . . 81
34 Isomorphic Quotients . . . . . . . . . . . . . . . . . . 81
35 Classiﬁcation of Modules . . . . . . . . . . . . . . . . 81
36 Abelian Groups of order 5 6 · 75 . . . . . . . . . . . . 82
37 Abelian Groups of order 108 . . . . . . . . . . . . . . 82
65

66 CHAPTER 3. MODULES
38 T/F Noetherian Modules . . . . . . . . . . . . . . . . . . 83
39 Diagonal Submodules . . . . . . . . . . . . . . . . . 83
40 Cyclic Product . . . . . . . . . . . . . . . . . . . . . 84
41 Simple Products . . . . . . . . . . . . . . . . . . . . 84
42 T/F Module Quotients . . . . . . . . . . . . . . . . . . . . 84
43 Indecomposable Modules . . . . . . . . . . . . . . . . 85
44 T/F Matrix Subrings . . . . . . . . . . . . . . . . . . . . . 85
45 T/F Schur’s Lemma Converse . . . . . . . . . . . . . . . . 86
46 T/F Noetherian Modules . . . . . . . . . . . . . . . . . . 86
47 T/F Zero-Divisors in Group Algebras . . . . . . . . . . . 86
48 T/F Commutative Semi-simple Rings . . . . . . . . . . . 87
49 Idempotents and J(R) . . . . . . . . . . . . . . . . . 87
50 T/F Nilpotent Ideal . . . . . . . . . . . . . . . . . . . . . 87
51 T/F Nilpotency in Semi-simple Rings . . . . . . . . . . . 87
52 Semi-simple Rings of order 4 . . . . . . . . . . . . . 87
53 T/F Jacobson Radical . . . . . . . . . . . . . . . . . . . . 88
54 T/F Semi-simple Rings . . . . . . . . . . . . . . . . . . . 88
55 Jacobson Radical of Z/m . . . . . . . . . . . . . . . 88
56 Idempotents and Jacobson Radicals . . . . . . . . . 88
57 Jacobson Radical of Matrices . . . . . . . . . . . . . 89
58 Nakayama’s Lemma . . . . . . . . . . . . . . . . . . 90
59 T/F Jacobson Radical . . . . . . . . . . . . . . . . . . . . 90
60 Jacobson Radicals of PIDs . . . . . . . . . . . . . . . 90
61 Nakayama’s Lemma . . . . . . . . . . . . . . . . . . 90
62 T/F Schur’s Lemma . . . . . . . . . . . . . . . . . . . . . 90
63 Semi-simple Rings . . . . . . . . . . . . . . . . . . . 91
64 T/F Division Rings . . . . . . . . . . . . . . . . . . . . . 91
65 T/F Division Algebras . . . . . . . . . . . . . . . . . . . . 91
66 T/F Simple Artinian Rings . . . . . . . . . . . . . . . . . 92
67 Group Algebras . . . . . . . . . . . . . . . . . . . . . 92
68 Group Algebras . . . . . . . . . . . . . . . . . . . . . 93
69 T/F Commutative Algebras . . . . . . . . . . . . . . . . . 93
70 T/F Commutative Algebras . . . . . . . . . . . . . . . . . 94
71 Simple Modules over Algebras . . . . . . . . . . . . . 94
72 Finite Rings . . . . . . . . . . . . . . . . . . . . . . . 95
73 Finite Simple Rings . . . . . . . . . . . . . . . . . . . 95
74 T/F Complex Algebra Dimensions . . . . . . . . . . . . . 95
75 Division Rings . . . . . . . . . . . . . . . . . . . . . 96
76 T/F Division Rings . . . . . . . . . . . . . . . . . . . . . 96
77 T/F Complex dimension 4 Algebras . . . . . . . . . . . . 97
78 T/F Complex dimension 3 Algebras . . . . . . . . . . . . 97
79 Rings of idempotents . . . . . . . . . . . . . . . . . . 97
80 T/F Nilpotent Free Rings . . . . . . . . . . . . . . . . . . 97
81 Real Algebras of Dimension 2 . . . . . . . . . . . . . 97
82 Similar Matrices . . . . . . . . . . . . . . . . . . . . 98
83 Similar Matrices . . . . . . . . . . . . . . . . . . . . 98
84 Nilpotent Matrices . . . . . . . . . . . . . . . . . . . 99
85 T/F Similarity Classes . . . . . . . . . . . . . . . . . . . . 99
86 Similarity Class of F2 . . . . . . . . . . . . . . . . . . 99
87 Simultaneous Diagonalization . . . . . . . . . . . . . 100
88 Simultaneous Diagonalization . . . . . . . . . . . . . 100
89 Matrices and Polynomials . . . . . . . . . . . . . . . 101
90 Minimal Polynomials . . . . . . . . . . . . . . . . . . 103
91 Matrix Relations . . . . . . . . . . . . . . . . . . . . 103

Algebra – James Wilson 67
92 Linear Decomposition . . . . . . . . . . . . . . . . . 103
93 Jordan Normal Form . . . . . . . . . . . . . . . . . . 104
94 Jacobson Module . . . . . . . . . . . . . . . . . . . . 104
95 Simple Algebras . . . . . . . . . . . . . . . . . . . . . 104
96 Endomorphisms and Semi-simplicity . . . . . . . . . 105
97 T/F Indecomposable Modules . . . . . . . . . . . . . . . . 105
98 Maximal Ideals . . . . . . . . . . . . . . . . . . . . . 105
99 T/F Polynomial Rings . . . . . . . . . . . . . . . . . . . . 106
100 T/F Injective Modules . . . . . . . . . . . . . . . . . . . . 106
101 Non-projective Modules . . . . . . . . . . . . . . . . 106
102 Projective Z-modules . . . . . . . . . . . . . . . . . . 107
103 Non-projective Modules . . . . . . . . . . . . . . . . 108
104 Cyclic Projective Modules . . . . . . . . . . . . . . . 108
105 Projective/Injective Inheritance . . . . . . . . . . . . 108
106 Injective Z/nZ-modules . . . . . . . . . . . . . . . . 109
107 T/F Injective Z-modules . . . . . . . . . . . . . . . . . . . 109
108 T/F Projectives over PIDs . . . . . . . . . . . . . . . . . 110
109 Module Quotients . . . . . . . . . . . . . . . . . . . . 110
110 Injectivity of Fraction Fields . . . . . . . . . . . . . . 110
111 T/F Injective Hulls . . . . . . . . . . . . . . . . . . . . . . 111
112 Semi-simple Modules . . . . . . . . . . . . . . . . . . 111
113 T/F Semi-simple Modules . . . . . . . . . . . . . . . . . . 111
114 T/F Projective R[x]-modules . . . . . . . . . . . . . . . . 111
115 T/F Projectivity and Freeness . . . . . . . . . . . . . . . 112
116 Dual Modules . . . . . . . . . . . . . . . . . . . . . . 112
117 Duals of Projectives . . . . . . . . . . . . . . . . . . 112
118 Finite Dimensional Duals . . . . . . . . . . . . . . . 113
119 Projectivity and Fields . . . . . . . . . . . . . . . . . 113
120 Subring Tensors . . . . . . . . . . . . . . . . . . . . . 114
121 Tensors over PIDs . . . . . . . . . . . . . . . . . . . 114
122 T/F Torsion and Tensors . . . . . . . . . . . . . . . . . . 115
123 T/F Fraction Field Tensors . . . . . . . . . . . . . . . . . 115
124 T/F Tensor Isomorphisms . . . . . . . . . . . . . . . . . . 116
125 Tensors and Quotients . . . . . . . . . . . . . . . . . 116
126 Tensors of Exact Sequences . . . . . . . . . . . . . . 117
127 Flat Modules . . . . . . . . . . . . . . . . . . . . . . 118
128 Induced Quotient Modules . . . . . . . . . . . . . . . 119
129 T/F Tensored Maps . . . . . . . . . . . . . . . . . . . . . 120
130 Endomorphism Rings and Tensors . . . . . . . . . . 120
131 Induced Modules over Tensors . . . . . . . . . . . . . 121
132 T/F Dimension and Tensors . . . . . . . . . . . . . . . . . 121
133 T/F Annihilating Modules . . . . . . . . . . . . . . . . . 121
134 T/F Identity Tensor . . . . . . . . . . . . . . . . . . . . . 122
135 T/F Tensors over Free Modules . . . . . . . . . . . . . . . 122
136 T/F Applied Tensors . . . . . . . . . . . . . . . . . . . . . 122
137 T/F Applied Tensors . . . . . . . . . . . . . . . . . . . . . 122
138 T/F Applied Tensors . . . . . . . . . . . . . . . . . . . . . 122
139 T/F Applied Tensors . . . . . . . . . . . . . . . . . . . . . 122
140 T/F Quotients and Tensors . . . . . . . . . . . . . . . . . 122
141 Mixed Ring Tensors . . . . . . . . . . . . . . . . . . 123
142 T/F Fields and Tensors . . . . . . . . . . . . . . . . . . . 123

68 CHAPTER 3. MODULES
1 Noetherian/Artinian Rings. Let K be an inﬁnite ﬁeld extension of k.
Let R be the ring of all 2 × 2 upper triangular matrices:
(α β
0 c
)
with α,β ∈K and c ∈k. Show that R is left artinian and left noetherian but
is neither right artinian nor right noetherian.
Example: The submodules of RR are nothing more than the left ideals of R
as left translation must be closed in each submodule. Given any ideal S of R,
we take A ∈S and B ∈R and observe:
BA =
(α β
0 c
)(α′ β′
0 c′
)
=
(αα′ αβ′ +βc′
0 cc′
)
.
AsA comes from an ideal S, then BA is in S. The multiplication above demon-
strates that the projection maps π1,1 : R → K and π2,2 : R → k are ring
homomorphisms (the addition is clearly preserved) and so they tell us that
π1,1(BA) ∈π1,1(S); π2,2(BA) ∈π2,2(S).
Indeed, π1,1(S) is an ideal of K and π2,2(S) is an ideal of k. As both K and k
are ﬁelds we have only the trivial choices of ideals. Therefore the components
A1,1 andA2,2 correspond to the two ideals of their respective ﬁelds which gives
us an up bound of four choices for the ideals in these components.
However, the component (BA)1,2 illustrates the fact that the projection map
π1,2 :R →K is not a ring homomorphism as multiplication is not preserved.
So now we know we may take
S =
[I T
0 J
]
where I ⊴K and J ⊴k, and T a subset of K closed under addition and with
the property that KT +KJ ⊆T ⊆K. If J =k then
KJ =Kk =K ≤T ⊆K; T =K.
So assume we have J = 0. Then we simply have the requirement that KT ⊆
T ⊆ K, and I does not factor into the problem at all. Clearly then 0 ∈ T if
T is non-empty – which it must be as otherwise matrices in S would not have
an upper right corner. Moreover, if there is a non-zero element a ∈ T , then
a−1 ∈ K so 1 ∈ T and then from here clearly K ⊆ T ⊆ K forcing once again
T =K. Thus we have the following list of left ideals:
[0 0
0 0
]
,
[K 0
0 0
]
,
[0 K
0 0
]
,
[K K
0 0
]
,
[0 K
0 k
]
,
[K K
0 k
]
.
As there are only ﬁnitely many left ideals, the ring is trivially left artinian and
left noetherian.
Now consider the right ideals. Given K/k is inﬁnite, it follows there is a
basis B = {bi : i ∈ I} for K/k as a vector space which is inﬁnite. Certainly
kn =Spank{b0,...,b n} is an inﬁnite ascending chain of distinct k-vector spaces
in K. Moreover, this induces the same in the RR:
Sn =
(0 kn
0 0
)
.

Algebra – James Wilson 69
Therefore RR is not right noetherian. With the similar construction: k′
n =
Spank{Bi :i ∈I\{0,...,n }} we see RR is neither right artinian as this is an
inﬁnite descending chain. 1 □
2 D.C.C. submodules and quotients. Let V be a left R-module and Hint: Use the correspondence
theorem and the second iso-
morphism theorem.
W ≤V be a submodule. Then V satisﬁes the D.C.C. if and only if W andV/W
do.
Proof: Suppose V satisﬁes the D.C.C. Given any chain of submodules in W ,
certainly these are submodules of V so they stabilize in ﬁnitely many steps in
V , and so too in W . Likewise, given any chain of submodules in V/W , by the
correspondence theorem we have a chain of submodules in V whose factors are
the original chain in V/W . Thus in V they stabilize so in V/W they stabilize.
Now suppose V/W and W satisfy the D.C.C. Take a chain
V0 ≥V1 ≥ · · ·
in V . This induces the chains:
V0 +W/W ≥V1 +W/W ≥ · · · ; V0 ∩W ≥V1 ∩W ≥ · · · .
As both V/W and W satisfy the D.C.C. it follows both these chains stabilize.
Now we use the 2nd isomorphism theorem to replace our chain in V/W with:
V0/V0 ∩W ≥V1/V1 ∩W ≥ · · · ,
which must also stabilize in ﬁnitely many steps as it is isomorphic to the chain
in V/W . Since the quotients and the intersections stabilize, and we have an
abelian group, the original chain stabilizes. □
3 Modules over artinian Rings. If R is left artinian and V is a ﬁnitely Hint: Resolve the module
with a ﬁnitely generated free
R-module, then use Exercise-
3.2.
generated left R-module then V satisﬁes D.C.C.
Proof: GivenV is ﬁnitely generated, it follows it has a generating set {a1,...,a n},
and so the free module Rn maps canonically onto V . Therefore V is a quotient
module of Rn. However, from Exercise- 3.2 we know if Rn satisﬁes D.C.C., then
so must the quotient V . Therefore we need only prove Rn satisﬁes D.C.C.
Given R is left artinian we know every chain of left ideals in R has ﬁnite
length. In R ⊕R we have the canonical embedding R ⊕ 0 of R, and we notice
that by projecting we obtain R ⊕R/R ⊕ 0 ∼= R. Hence, using Exercise- 3.2 in
reverse we see that R2 satisﬁes the D.C.C. as a left R-module. Now we induct.
Let Rk satisfy the descending chain condition. As such, Rk+1/Rk ⊕ 0 ∼= R so
once again by Exercise- 3.2 we know Rk+1 to also satisfy the descending chain
condition as a left R-module. Therefore by induction we may now conclude that
Rn satisﬁes the descending chain condition and as use so does V . □
4 Sum decomposition of A.C.C./D.C.C. Assume that a left R-module V Hint: Show that extensions
of A.C.C. modules are A.C.C.,
then induct.
is written as a ﬁnite sum of its submodules:
V =
n∑
i=1
Vi.
Show that V is noetherian (resp. artinian) if and only if so is every Vi.
1When multiplying from the right, the matrix A spans R and B is ﬁxed in S; thus, the
term T = IK + T k which is K, or any k vector space.

70 CHAPTER 3. MODULES
Proof: Suppose V satisﬁes the ascending chain condition as a left R-module.
Then given that each Vi is a submodule of V , any ascending chain of submodules
of Vi is also one in V . Hence, the length of this chain must be ﬁnite in V so
it must also be ﬁnite in Vi. In conclusion each Vi satisﬁes the ascending chain
condition. The same argument follows mutatis mutandis for the descending
chain condition.
Now take each Vi to satisfy the ascending chain condition. Suppose also
for induction that ∑k
i=1Vi satisﬁes the ascending chain condition. First as the
additive structure is an abelian group, we know ∑k
i=1Vi is a subgroup of V since
all the submodules Vi are normal subgroups. Furthermore, given any r ∈R,
r
( k∑
i=1
Vi)
)
=
k∑
i=1
rVi ⊆
k∑
i=1
Vi.
using the fact that each Vi is indeed a submodule. Hence ∑k
i=1Vi is a submod-
ule, and moreover, so is ∑k+1
i=1 Vi. Finally,
k+1∑
i=1
Vi/
k∑
i=1
Vi ∼=Vk+1/
( k∑
i=1
Vi
)
∩Vk+1.
Since Vk+1 satisﬁes the ascending chain condition, so does
Vk+1/Vk+1/
( k∑
i=1
Vi
)
∩Vk+1.
If we show that an extension of A.C.C. modules is A.C.C. we will have the right
to conclude that V is A.C.C. by induction.
Now suppose V/W and W satisfy the A.C.C. Take a chain
V0 ≤V1 ≤ · · ·
in V . This induces the chains:
V0 +W/W ≤V1 +W/W ≤ · · · ; V0 ∩W ≤V1 ∩W ≤ · · · .
As both V/W and W satisfy the A.C.C. it follows both these chains stabilize.
Now we use the 2nd isomorphism theorem to replace our chain in V/W with:
V0/V0 ∩W ≤V1/V1 ∩W ≤ · · · ,
which must also stabilize in ﬁnitely many steps as it is isomorphic to the chain
in V/W . Since the quotients and the intersections stabilize, the original chain
stabilizes. □
5 Module Bases. Let k be a ﬁeld and V be a vector space over k withHint: Verify the the claim di-
rectly. an inﬁnite basis {e0,e 1,... }, and R = Endk(V ). Let r,s ∈ R be the elements
deﬁned by r(e2n) = en, r(e2n+1) = 0 and s(e2n) = 0, s(e2n+1) = en. Prove
{r,s } is a basis of R.
Proof: Takeϕ,ψ ∈R so that ϕr +ψs = 0. If we evaluate
ϕ(en) = ϕr(e2n) +ψs(e2n) = 0;ψ(en) = ϕr(e2n+1) +ψs(e2n+1) = 0.
Therefore ϕ = 0 and ψ = 0 so {ϕ,ψ } are linearly independent. Furthermore
deﬁne for every ϕ ∈R
ϕe(ei) = ϕ(e2i); ϕo(ei) = ϕ(e2i+1).

Algebra – James Wilson 71
So
ϕe(r(e2i)) +ϕo(s(e2i)) = ϕe(ei) = ϕ(e2i)
and
ϕe(r(e2i+1)) +ϕo(s(e2i+1)) = ϕe(ei) = ϕ(e2i+1).
Thus,ϕ =ϕer +ϕos so {r,s } is a basis for R. □
6 Uniqueness of Module Decomposition. – True or False? Let V = Hint: Consider non-cyclic ﬁ-
nite Z-modules.W ⊕X andV =W ⊕Y be decompositions of a left R-module v as direct sums
of modules. Then X =Y .
Example: Consider V = Z2 ⊕ Z2 as Z-module. The decompositions
⟨(1, 0)⟩ ⊕ ⟨(0, 1)⟩; ⟨(1, 0)⟩ ⊕ ⟨(1, 1)⟩
do not agree but they both are decompositions of V .
If you allow W to vary then it is worse: X need not be isomorphic to Y ;
consider
Z2 ⊕ Z6 = (Z2 ⊕ Z2) ⊕ Z3.
□
7 Maschke’s Theorem. LetG be a ﬁnite group, F a ﬁeld of characteristic p Hint: Consider the augmenta-
tion ideal.dividing |G|, and FG the group algebra. Consider the 1-dimensional submodule
of the left regular module FGFG spanned by the element ∑
g∈Gg. Show that
this submodule is not a direct summand of the regular module.
Proof: Letx =∑
g∈Gg and take W be a complement to ⟨x⟩ in FGFG . Hence
we know
1 ∈FG FG = ⟨x⟩ ⊕W
so 1 = λx +w for some λ ∈ FG and w ∈ W ; that is, 1 −λx ∈ W . Therefore
for any g ∈G, g(1 −λx) ∈W since W is an FG -module. Indeed we may take
λ ∈F since gx =x it is clear that
λx =

∑
g∈G
cgg



∑
g∈G
g

 =

∑
g∈G
cg

x,
and each cg ∈F . Given that the characteristic of F divides the order of |G|, it
must follow that |G|λ = 0 in F . Also λ commutes with g so we get
∑
g∈G
g(1 −λx) =
∑
g∈G
g −gλx =
∑
g∈G
(g −λgx) =
∑
g∈G
(g −λx) = x − |G|λx =x.
However, above we resolved that this sum was in W so we must conclude that
x ∈ W which means that W does not split with ⟨x⟩ in FGFG . Therefore ⟨x⟩
has no complement proving FGFG is not semi-simple. □
8 Module Annihilators. – True or False? Hint: Consider the annihila-
tors of quotient modules.(a) Let R be a commutative ring with ideals I,J such that R/I ∼= R/J (as
modules), then I =J.
(b) Let R be any ring and I,J any two left-ideals where R/I and R/J are
isomorphic as left modules, then I =J.

72 CHAPTER 3. MODULES
(a) Proof: True. Given R is a commutative ring, it follows R →End(R/I) :
r ↦→r(1+I) has kernelI, and by deﬁnition this kernel is AnnR(R/I). Hence,
I =AnnR(R/I) and likewise J =AnnR(R/J ). As such, if R/I ∼=R/J as
R-modules, then we have AnnR(R/I) = AnnR(R/J ) so indeed I =J. □
(b) Example: False. With a non-commutative example we know that the
annihilator of a module is always a two sided ideal, so we need only choose
one sided ideals to defeat the proof above. So consider a non-commutative
ring R =M2(F ), with F a ﬁeld. Then the left ideals
I =
{[x 0
y 0
]}
, J =
{[0 x
0 y
]}
,
give the natural projection quotients:
R/I ∼=J, R/J ∼=I.
There is also a natural R-module isomorphism between I and J so indeed
R/I ∼=R/J . However, I ⁄=J visibly. □
9 Divisor Chains. Let R = C[[x]], the ring of formal power series overHint: Place the matrix for the
injection from W into V in
Rational Canonical Form.
C. Consider the submodule W of the free module V =Rv1 ⊕Rv2 generated by
u1 = (1 −x)−1v1 + (1 −x2)−1v2 and u2 = (1 +x)−1v1 + (1 +x2)−1v2.
Find a basis {v′
1,v ′
2} of V and elements δ1|δ2 ∈R such that W is generated by
δ1v′
1 and δ2v′
2. Describe V/W .
Example: We are asked to ﬁnd unimodular matrices P and Q such that we
have the following diagram:
0 /d47/d47Ru1 ⊕Ru2
A /d47/d47
Q
/d15/d15
Rv1 ⊕Rv2 /d47/d47
P
/d15/d15
V/W /d47/d47
/d15/d15
0
0 /d47/d47δ1Rv′
1 ⊕δ2Rv′
2
PAQ −1
/d47/d47Rv′
1 ⊕Rv′
2 /d47/d47R/δ1Rv′
1 ⊕R/δ2Rv′
2 /d47/d47 0.
We do this by computing the Rational Canonical Form for the matrix A. We
notice that if we let
A =
[ 1
1−x
1
1+x1
1−x2
1
1+x2
]
and considerR expressed according tov1 andv2, then we haveW =SpanR{Ae1,Ae 2},
with eT
1 = (1, 0) and eT
2 = (0, 1).
[ 1 0
− 1
1+x 1
][ 1
1−x
1
1+x1
1−x2
1
1+x2
]
=
[ 1
1−x
1
1+x
0 −1
(1+x)2 + 1
1+x2
]
;
[ 1
1−x
1
1+x
0 −1
(1+x)2 + 1
1+x2
][ 1 − 1−x
1+x
0 1
]
=
[ 1
1−x 0
0 −1
(1+x)2 + 1
1+x2
]
.
Since 1
1−x (1 −x) = 1 we know 1
1−x is a unit so it clearly divides 1
1+x2 − 1
(1+x)2
so our matrix is in rational canonical form. Therefore the elementary divisors
are δ1 = 1
1−x and δ2 = 1
1+x2 − 1
(1+x)2 . In the same way we have
P =
[ 1 0
− 1
1+x 1
]
, Q −1 =
[1 − 1−x
1+x
0 1
]
.

Algebra – James Wilson 73
Thus to transfer V from the basis {v1,v 2} to {v′
1,v ′
2} we simply use P .
[v′
1
v′
2
]
=P
[v1
v2
]
=
[ 1 0
−1
1+x 1
][v1
v2
]
=
[ v1
− v1
1+x +v2
]
.
Finally, under this new basis {v′
1,v ′
2} we see
V/W =R/
( 1
1 −x
)
⊕R/
( 1
1 +x2 − 1
(1 +x)2
)
∼= 0 ⊕R/(x) ∼= C
using the fact that 1
1−x is a unit and that
1
1 +x2 − 1
1 + 2x +x2 = 1 + 2x +x2
1 + 2x + 2x2 + 2x3 +x4 − 1 +x2
1 + 2x + 2x2 + 2x3 +x4
= 2x
1 + 2x + 2x2 + 2x3 +x4.
Since 1 + 2x + 2x2 + 2x3 +x4 ∈ C[[x]] it follows
R/
( 1
1 +x2 − 1
(1 +x)2
)
∼=R/(2x) ∼=R/(x).
□
10 Composition Series – True or False? Every ﬁnitely generated module Hint: Consider the integers.
over a commutative noetherian ring has a composition series.
Example: Consider Z. Certainly Z is noetherian as any ascending chain must
begin with 0,m Z, and from there there are only ﬁnitely many intermediate
submodules. However, Z is not artinian as piZ is an inﬁnite descending chain.
Since Z is ﬁnitely generated it has a composition series if and only if it is both
artinian and noetherian. Thus it has no composition series. □
11 Free Submodules – True or False? If R is a commutative ring then Hint: Consider ﬁnite rings.
any submodule of a free module is free.
Example: Consider Z4 over Z4. Certainly any ring over itself is free, and this is
also a commutative ring; yet, Z2 is a submodule over Z4 but it is not isomorphic
to a direct product of Z4 (ﬁnite means it is ﬁnitely generated as well) so Z2 is
not free over Z4. □
12 Free Submodules – True or False? If R is a domain then any Hint: Consider F [x,y ].
submodule of a free module is free.
Example: False. Consider a ﬁeld F , and its associated polynomial ring F [x,y ].
SinceF is an integral domain, so is F [x,y ]. However, if we take the left F [x,y ]
ideal (x,y ), then we notice the relation xy =yx. Yet x and y are independent
elements as y /∈ (x) and x /∈ (y). This means x,y cannot be a basis as there is
a relation, so ( x,y ) is not a free F [x,y ] module. □
13 Free PID Modules – True or False? IfR is a PID then any submodule Hint: Use the canonical repre-
sentation of ﬁnitely generated
modules over a PID.
of a ﬁnitely generated free R-module is free.
Proof: True. Let V be a ﬁnitely generated free R-module and W a submodule
ofV . From Theorem-3.7.7, and the fact that R is a PID, we know W is ﬁnitely
generated and
W ∼=R/δ1 ⊕ · · · ⊕R/δn

74 CHAPTER 3. MODULES
where d1| · · · |dn. Furthermore, as V is free, there can be no torsion in V or
in any submodule W ; therefore, each di = 0. So indeed, W is a ﬁnite direct
product of R’s so it is a free R module. □
14 Free Inheritance – True or False? If R is commutative and everyHint: Show any two genera-
tors have relations. submodule of a free R-module is free, then R is a PID.
Proof: Certainly RR is free so each of its submodules I is free. Suppose that
I has basis {a1,a 2,... }. As R is commutative it follows that a1a2 = a2a1 so
there is a non-trivial relation between the proposed basis. Hence a1 =a2 = · · ·
is required so indeed I is generated by a single element. Since every ideal of R
is a submodule, we see R is a PID. □
15 PID Quotients – True or False? IfR is a PID and I a proper ideal of RHint: Consider Z.
then R/I is a PID.
Example: Notice that what can fail is to have a quotient that is not an inte-
gral domain. For example, Z and 4Z has quotient Z/4Z which has zero-divisors;
thus, while it is a principle ideal ring, it is not a domain, so it is not a PID. □
16 PID subrings – True or False? If R is a PID, then any subring of R isHint: Consider Q[x].
a PID.
Example: As Q is a ﬁeld, Q[x] is a PID; however, Z[x] is a subring but not a
PID.
To see this consider the map:
0 /d47/d47I =Ker f /d47/d47 Z[x] /d47/d47 Z2 /d47/d47 0
given by f (p(x)) = p(0). This is simply an evaluation homomorphism so its
properties will not be veriﬁed explicitly. Also clearly f (1) = 1 and f (0) = 0 so
f is surjective so I ⁄= Z[x].
Notice also that I is simply all polynomials with even constant term, as
p(x) ∈ I whenever f (p(x)) = p(0) = p0 ∼= 0 (mod 2). Suppose I = (a(x)) for
some a(x) ∈ Z[x]. Hence we have 2 ∈ I and so there must exist a b(x) ∈ Z[x]
such that 2 = b(x)a(x) proving that deg a(x) = 0 so a(x) = ±1 or ±2. If
a(x) = ±1 then I = Z[x] – already seen to be false. If a(x) = ±2 then there
is no f (x) such that x = f (x)a(x), and so we conclude that I could not be
principle to begin with. □
17 Polynomials over PIDs – True or False? If R is a PID then R[x] is aHint: Consider Z.
PID.
Example: Let R = Z. Z[x] is not a PID. (See Exercise- 3.16.) □
18 Polynomials over Artinian Rings – True or False? If R is artinian,Hint: Consider (x) ≥ (x2) ≥
· · ·. R[x] is as well.
Example: Given any ring R, notice
(1) ≤ (x) ≤ (x2) ≤ (x4) ≤ · · · ≤ (x2i
) ≤ · · ·
so R[x] is not artinian. □
19 Torsion Free vs. Free – True or False? Any ﬁnitely generated torsionHint: Consider the canonical
presentation of modules over
PIDs.
free module over a PID is free.

Algebra – James Wilson 75
Proof: True. Since the module is ﬁnitely generated over a PID R it is equivalent
to a direct sum
M =R/(d1) ⊕ · · · ⊕R/(dk).
HoweverM is torsion free so each di = 0 as otherwise ei – the canonical com-
ponent generator – has non-trivial annihilator and thus has torsion. As such M
is truly just a direct sum of R modules, so consequently it is a free R module. □
20 Hom over PIDs Let R be a PID. Calculate HomR(R/(a),R/ (b)). Hint: Consider the greatest
common divisor of a and b.
Prove it by sending 1 in R to
the mapx+(a) ↦→ b
(a,b)x+(b)
in HomR(R/(a),R/ (b)).
Example: The solution is HomR(R/(a),R/ (b)) ∼=R/(a,b ) ∼=R/GCD (a,b ).
Deﬁne the map Λ : R →HomR(R/(a),R/ (b)) by
Λ(r)(x + (a)) = r b
GCD(a,b )x + (b)
forr,x ∈R. Since R is a PID, the greatest common divisor of a andb is deﬁned,
and furthermore, GCD(a,b )|b in R. To show that Λ is well-deﬁned take
x +sa ≡x (mod a).
From here it follows from the deﬁnition of Λ
Λ(r)(x +sa) ≡ r b
GCD(a,b ) (x +sa)
≡ r b
GCD(a,b )x +rs ab
GCD(a,b )
≡ Λ(r)(x) +rsLCM (a,b )
≡ Λ(r)(x) (mod b).
Since Λ(r) is left translation, it is clearly an R-module homomorphism between
R/(a) and R/(b), so Λ is well-deﬁned.
Now we brieﬂy demonstrate that Λ is R-linear itself:
Λ(rs +t)(x) ≡ (rs +t) b
GCD(a,b )x
≡ r
(
s b
GCD(a,b )x
)
+t b
GCD(a,b )x
≡ rΛ(s)(x) + Λ(t)(x)
≡ (rΛ(s) + Λ(t))(x) (mod b).
Next we demonstrate that Λ is epic so we may use the ﬁrst isomorphism
theorem. To see this take any g ∈HomR(R/(a),R/ (b)). Here we know
0 ≡g(0) ≡g(a · 1) ≡ag(1) (mod b).
However this then requires that b|ag(1), and clearly we also have a|ag(1), so
indeed, LCM (a,b )|ag(1). So there exists an r′ ∈R such that
ag(1) = r′LCM (a,b ) = r′ ab
GCD(a,b ) = (r′a) b
GCD(a,b ).
So if we let r = r′a then we have Λ( r)(1) = g(1) so indeed by the linearity,
Λ(r) = g.
Finally we must determine the kernel of Λ to prove our assertion. Take any
r ∈R such that Λ(r)(x) ≡ 0 (mod b) for all x ∈R. It follows then when x = 1
that
0 ≡ Λ(r)(1) ≡r b
GCD(a,b ) (mod b)

76 CHAPTER 3. MODULES
and therefore GCD(a,b )|r. Hence r ∈ (GCD(a,b )). And as expected, if we
take
Λ(rGCD (a,b ))(x) ≡rGCD (a,b ) b
GCD(a,b )x ≡rbx ≡ 0 (mod b).
So Ker Λ = (GCD(a,b )); thus, by the ﬁrst isomorphism theorem we now can
say – as R-modules:
R/(GCD(a,b )) ∼=HomR(R/(a),R/ (b)).
□
21 Pure Submodules LetR be a PID, and V andR-module. A submoduleHint: Show W contains
the torsion submodule then
use the canonical presentation
for ﬁnitely generated modules
over PIDs.
W ≤V is called pure ifW ∩rV =rW for all r ∈R. If V is a ﬁnitely generated
R-module, prove that a submodule W ≤ V is a pure submodule if and only if
W is a direct summand of V .
Proof: Given V =W ⊕U take any v ∈V to be v =w +u with w ∈W and
u ∈U . Certainly rv =rw +ru and rv ∈rW if and only if ru =rv −rw ∈rW
as clearly rw ∈rW . Thus ru = 0 since W ∩U = 0. Hence u = 0 as this works
for all r ∈R. Therefore v =w proving
W ∩rV =rW.
Now suppose that W is a pure submodule of V . Given any r ∈R such that
rv +W = W , it follows rv ∈ W , so rv ∈ W ∩rV = rW . This implies v ∈ W
to begin with. So indeed, V/W is torsion-free. Hence the torsion submodule of
V is contained in W . Since V is ﬁnitely generated over a PID, and V/T (V ) is
torsion-free, it follows V/T (V ) is free and W/T (V ) remains a pure submodule
of V/W . If W/T (V ) is a direct summand of V/T (V ) then by the correspon-
dence theorem we know W is a direct summand of V . However, as V/T (V ) is
free and W/T (V ) a submodule, we know there exists a suitable basis and suit-
able elementary divisors to present W/T (V ). However, the second isomorphism
theorem tells us ( V/T (V ))/(W/T (V )) ∼= V/W which is torsion free, so each
elementary divisor must be a unit or 0. Hence W/T (V ) is a direct summand of
V/T (V ) and so W is a direct summand of V . □
22 Invariant Factors Calculate the invariant factors of the followingHint: Use the norm to de-
termine which Gaussian inte-
gers are units and which are
irreducible. Also recall that
the Gaussian integers are a
Euclidean Domain so the Eu-
clidean algorithm applies.
matrices, working over Z[i] of Gaussian Integers:


1 0 0
0 1 + i 0
0 0 2 + i

 and


2i i 2 +i
i − 1 1 + i 0
0 0 2 + i
1 +i −1 2 + i

.
Example: First we recall a useful tool for working with commutative ring
extensions. The norm function N : Z[i] → Z :x =a +bi →xx =a2 +b2 sends
units to units. So if the norm of a number is invertible, only then is the element
invertible in Z[i]. Also, as N (xy) = N (x)N (y) it follows if N (x) is irreducible
then so is x. Thus using the Smith Normal Form algorithm in the ﬁrst matrix
we notice we need only work on the minor with top corner 2 , 2. Here we add
column 3 to column 2 ﬁrst so that a2,2 ∤a2,3.


1 0 0
0 1 + i 0
0 0 2 + i




1 0 0
0 1 0
0 1 1

 =


1 0 0
0 2 + i 0
0 1 + i 1 +i

.

Algebra – James Wilson 77
Using the Euclidean algorithm we ﬁnd the greatest common divisor (2 + i, 1 +i):
2 +i = (1)(1 + i) + 1;
1 +i = (1 + i)(1) + 0.
As such we have 1 as the GCD and moreover
1 = (1)(2 + i) + (−1)(1 +i).
We also know from the proof of the Smith Normal Form algorithm that there
exists d1,d 2 ∈ Z[i] such that
1 = (1)d1 + (−1)d2; d1 = 1, d 2 = 0.
Finally it follows the following matrix reduces our irreducible 2 + i by some
number of irreducible factors, so in our situation it must reduce to a unit allowing
us to complete the normal form by recursion on the algorithm.


1 0 0
0 1 −1
0 1 0




1 0 0
0 2 + i 0
0 1 + i 1 +i

 =


1 0 0
0 1 −1 −i
0 2 + i 0

.
Now that a2,2 is a unit we use it to clear the second row and column.


1 0 0
0 1 0
0 −2 −i 1




1 0 0
0 1 −1 −i
0 2 + i 0

 =


1 0 0
0 1 −1 −i
0 0 1 + 3 i

,


1 0 0
0 1 −1 −i
0 0 1 + 3 i




1 0 0
0 1 1 + i
0 0 1

 =


1 0 0
0 1 0
0 0 1 + 3 i

.
The invariant factors are thus 1 , 1, 1 + 3i. Now we move the the challenging
matrix.
PENDING: redo Notice that 2 + i is a unit and common to every term in
the third column. So we clear the third column.


1 0 −1 0
0 1 0 0
0 0 1 0
0 0 −1 1




2i i 2 +i
−1 +i 1 +i 0
0 0 2 + i
1 +i −1 2 + i

 =


2i i 0
−1 +i 1 +i 0
0 0 2 + i
1 +i −1 0

.
Next we notice that adding row 4 to row 2 leaves the ﬁrst row.


1 0 0 0
0 1 0 1
0 0 1 0
0 0 0 1




2i i 0
−1 +i 1 +i 0
0 0 2 + i
1 +i −1 0

 =


2i i 0
2i i 0
0 0 2 + i
1 +i −1 0

.
Now delete the superﬂuous row 2.


1 0 0 0
−1 1 0 0
0 0 1 0
0 0 0 1




2i i 0
2i i 0
0 0 2 + i
1 +i −1 0

 =


2i i 0
0 0 0
0 0 2 + i
1 +i −1 0

.
Now we move our units into the diagonal.


0 0 1 0
0 0 0 1
1 0 0 0
0 1 0 0




2i i 0
0 0 0
0 0 2 + i
1 +i −1 0




0 0 1
0 1 0
1 0 0

 =


2 +i 0 0
0 −1 1 + i
0 i 2i
0 0 0

.

78 CHAPTER 3. MODULES
Finally we use the unit −1 to clear the second row and second column.


1 0 0 0
0 1 0 0
0 i 1 0
0 0 0 1




2 +i 0 0
0 −1 1 + i
0 i 2i
0 0 0

 =


2 +i 0 0
0 −1 1 + i
0 0 −1 + 3i
0 0 0

.


2 +i 0 0
0 −1 1 + i
0 0 −1 + 3i
0 0 0




1 0 0
0 1 1 + i
0 0 1

 =


2 +i 0 0
0 −1 0
0 0 −1 + 3i
0 0 0

.
Finally we clean it up a little:


(2 +i)−1 0 0 0
0 −1 0 0
0 0 1 0
0 0 0 1




2 +i 0 0
0 −1 0
0 0 −1 + 3i
0 0 0

 =


1 0 0
0 1 0
0 0 −1 + 3i
0 0 0

.
The invariant factors are 1 , 1, −1 + 3i but as this unique up to
units we may say it is 1 , 1, −1 + 3i. □
23 Smith Normal From LetHint: The invariant factors
are 1, 2, 6.
A =


−4 −6 7
2 2 4
6 6 15

.
Find unimodular matrices X and Y such that XAY has the Smith Normal
form: diagonal matrix with a divisor chain along the diagonal.
Example:


0 1 0
1 0 0
0 0 1




−4 −6 7
2 2 4
6 6 15

 =


2 2 4
−4 −6 7
6 6 15

,


2 2 4
−4 −6 7
6 6 15




1 −1 −2
0 1 0
0 0 1

 =


2 0 0
−4 −2 15
6 0 3

,


1 0 0
2 1 0
−3 0 1




2 0 0
−4 −2 15
6 0 3

 =


2 0 0
0 −2 15
0 0 3

,


2 0 0
0 −2 15
0 0 3




1 0 0
0 1 7
0 0 1

 =


2 0 0
0 −2 1
0 0 3

,


2 0 0
0 −2 1
0 0 3




1 0 0
0 0 1
0 1 0

 =


2 0 0
0 1 −2
0 3 0

,


1 0 0
0 1 0
0 −3 1




2 0 0
0 1 −2
0 3 0




1 0 0
0 1 2
0 0 1

 =


2 0 0
0 1 0
0 0 6

,


0 1 0
1 0 0
0 0 1




2 0 0
0 1 0
0 0 6




0 1 0
1 0 0
0 0 1

 =


1 0 0
0 2 0
0 0 6

.
□

Algebra – James Wilson 79
24 Invariant Factors – True or False? Let R be a PID and V be aHint: Recall invariant factors
are unique. ﬁnitely generated R-module with invariant factors δ1|δ2| · · · |δk. Then V cannot
be generated by less than k elements.
Proof: True. Take V to be generated by {g1,...,g n} and relators
f1(g1,...,g n) = 0,...,f k(g1,...,g n) = 0
forfi ∈R[x1,...,x n]. Then V is equivalently described by a n ×k matrix over
R Γ. This matrix Γ is equivalent to a unique Smith normal form (diagonal
matrix with a divisor chain along the diagonal) Γ ′. Given any other generating
set, this process must produce the same Smith normal as this is an invariant
of the module V . Therefore, as each time the number of invariant factors (the
non-zero, non-unit divisors along the diagonal) is less than or equal to the num-
ber of generators n (they lie along the diagonal which has length less than or
equal to n), it follows the number of invariant factors is the minimum number
of generating elements for V . □
25 Left Regular Modules – True or False? Let R be a commutative ring. Hint: For the ﬁrst consider
ﬁnite rings, for the second
use the canonical representa-
tion of modules over a PID.
Is it true that the left regular R-module is indecomposable? What if R is a
PID?
(a) Example: False. Consider Z6 ∼= Z2 ⊕ Z3. As a Z2 and Z3 are ideal of Z6
they are acceptable Z6-modules. Moreover, they decompose Z6 proving it
is not indecomposable. □
(b) Proof: True. The addition of the PID condition tells us we can use the
canonical presentation of ﬁnitely generated modules over a PID.
TakeRR to be decomposed into a direct product of submodules W1,...,W n.
As 1 generates RR it follows RR is a ﬁnitely generated module over a PID
R; therefore, there exists a generating set for RR such that Wi ∼= R/(di)
and so that:
RR ∼=R/(d1) ⊕ · · · ⊕R/(dn)
where d1| · · · |dn – and we allow di = 0 if free terms appear.
Now we notice that RR is torsion free as sr = 0 implies r = 0 or s = 0 as
we have an integral domain. Hence we may take di = 0 for all i = 1,...,n .
However now we notice that the rank of RR isn, but clearly a basis for RR
is 1. Since R is a commutative ring as a regular module it is rank invariant,
so indeed n = 1. Therefore there is not proper decomposition of RR when
R is a PID. □
26 Matrix Equivalence – True or False? LetR be a PID and A andn ×n Hint: The product of unimod-
ular matrices is unimodular.matrix over R. Then A is invertible if and only if A is equivalent to the identity
matrix.
Proof: True. Given A is invertible it follows A−1 exists. Moreover, A−1 is also
invertible so it is trivially unimodular. With this we can directly see that the
equivalence
A−1AIn =In
where the unimodular transformation matrices are A−1 and In.

80 CHAPTER 3. MODULES
For the converse take
PAQ =In
with P and Q unimodular. It follows then that both P and Q are invertible so
A =P −1InQ−1 = (QP )−1.
As Q and P are unimodular so is their product, and so their inverse is as well;
hence, A is unimodular and so invertible. □
27 Invariant Factors Find the invariant factors and the primary decompo-Hint: Primary decomposition
corresponds to prime factor-
ization in Z.
sition for Z/2000Z.
Example: Given 2000 = 2 4 · 53 and Z/2000Z is cyclic it follows its invariant
factor is simply 2000 while its primary decomposition is simply
Z/2000Z = Z/(24) ⊕ Z/(53).
□
28 Primary Decomposition Letp be a prime and V be a ﬁnitely generatedHint: Determine that p di-
vides each invariant factor. Z-module with paV = 0. Suppose that v ∈V has order exactly pa. Show that
V = Zv ⊕W for some submodule W ≤V .
Proof: Since Z is a PID, and V is ﬁnitely generated it follows V decomposes as
Z/d1 ⊕ · · · Z/dk where d1|d2| · · · |dk and di is a non-unit but possibly 0. Notice
since paV = 0 that p|di for all i, and di ≤ pa. Moreover, as there exists an
element of order exactly pa, it follows some di = pa. Since v may be chosen,
without loss of generality, to lie in this component of the decomposition we now
see we may take as the complement of Zv the remaining Z/di’s. □
29 Endomorphisms over PIDs – True or False? Let V be a ﬁnitelyHint: Show ﬁrst V is simply a
direct sum of Q[t]’s. generated torsion free Q[t]- module, and τ ∈EndQ[t](V ) be surjective; then τ is
injective.
Proof: True. Given this Q[t] is a PID we may decompose the ﬁnitely generated
torsion free module V into a ﬁnite direct sum of Q[t]. Given an endomorphism
τ that is surjective we know the ﬁrst isomorphism theorem applies so that
V/Ker τ ∼= V . Now suppose x is a non-trivial element of the kernel of τ . It
follows Q[t]x ≤Kerτ . However V is torsion free so Ann(x) = 0 so Q[t]x ∼= Q[t];
thus,
Ker τ ∼= Q[t] ⊕ · · · ⊕ Q[t].
Now we must concern ourselves with a possible “diagonal” embedding. Let
{e1,...,e n} represent a basis forV . Then if Q[t]ei∩Kerτ ⁄= 0 then Q[t]ei/Kerτ ∩
Q[t]ei must be trivial or else it will have torsion; whence ei ∈Ker τ. Therefore
Ker τ reduces the rank of V .2 Since the rank is ﬁnite reducing the rank cannot
be surjective. Therefore the kernel must be trivial. □
30 Endomorphisms over PIDs – True or False? Let V be a ﬁnitelyHint: Consider translation by
t. generated torsion free Q[t]-module, and τ ∈ EndQ[t](V ) be injective; then τ is
surjective.
Example: False. The translation by t map τ (x) = tx is always an endomor-
phism; however, the element t has no inverse in Q[t] so indeed τ is not surjective
as it will not hit 1. □
31 Torsion Free vs. Free – True or False? A (not necessarily ﬁnitelyHint: Consider Q as a Z-
module. 2Rank of free modules over a commutative ring is invariant.

Algebra – James Wilson 81
generated) torsion-free module over a PID is free.
Example: False. Given Q as an additive group is a Z-module we see for any
q ∈ Q, nq = 0 implies n = 0 or q = 0 as Q is an integral domain and n ∈ Q
whenevern ∈ Z. Hence, Q is torsion-free.
Yet, Q is not a free Z-module as it has no basis. Consider any two rational
numbersa/b and c/d. Clearly
(cb)a
b + (−ad)c
d =ac −ac = 0
so a
b and c
d are linearly dependent. So as Z ⁄= Q, Q is not free of rank 1, and
by the above it is not free of a higher rank – so Q is not free as a Z-module. □
32 Rank Ordering – True or False? Let V <W be a proper containment Hint: Consider V =Z Z and
its submodules.of free Z-modules; then rankZV <rank ZW .
Example: False. Consider 2 Z < Z. As Z is commutative 2 Z is an ideal and
so a submodule. Moreover, Z ∼= 2Z so it is a free Z-module. Finally, as they
are isomorphic, and rank in commutative rings is invariant, it follows they both
have rank 1, not one less than the other. □
33 Free Quotients – True or False? IfV ≤W are free Z-modules of equal Hint: Express V in terms of
the same basis as W .ﬁnite rank, then W/V is a ﬁnite group.
Proof: True. Since both are ﬁnitely generated modules over a PID we may
select a basis {e1,...,e n} for W such that V is precisely
V = (δ1Z)e1 ⊕ · · · ⊕ (δnZ)en
with δ1| · · · |δn and none of the δi’s units. Furthermore, as V and W have the
same rank it follows n =rank V =rank W, and also di ⁄= 0 for any i – as for
then the rank of W would be less than that of V .
Now the quotient is visibly isomorphic to:
W/V ∼= Z/(δ1) ⊕ · · · ⊕ Z/(δn)
with each δi a positive integer. Clearly now we know the size of the quotient to
be δ1 · · ·δn which is ﬁnite. □
34 Isomorphic Quotients The C[x,y ]-modules C[x,y ]/(x,y ) and C[x,y ]/(x− Hint: Recall Exercise-
??.3.17.8 part (a) – annihila-
tors of isomorphic quotients
must agree.
1,y − 1) are isomorphic.
Proof: False. Note from Exercise- ??.3.17.8 part (a) we already know that two
quotient modules of a commutative ring are isomorphic only when the ideals
agree. So we need only show ( x,y ) ⁄= (x − 1,y − 1).
To do this suppose p(x,y ),q (x,y ) ∈ C[x,y ] so that
x =p(x,y )(x − 1) +q(x,y )(y − 1) = p(x,y )x −p(x,y ) +q(x,y )y −q(x,y ).
As y is not a unit nor does it divide x, it follows that q(x,y ) = 0 is required,
and p(x,y ) must really be a polynomial in x only. However then we allowed to
take about degrees so we have
1 = deg x=deg p(x)(x − 1)
which requires p(x) be a constant. As 1 is not a zero-divisor it is clear that no
suchp(x) exists so indeed x /∈ (x − 1,y − 1) so (x,y ) ⁄= (x − 1,y − 1) and so the
two quotient modules are not isomorphic. □

82 CHAPTER 3. MODULES
35 Classiﬁcation of Modules Classifying, up to isomorphism, all Q[t]- Hint: Consider ideals which
containI. This are the annihi-
lators of the possible modules.
modulesV which are annihilated byI = ((t3−2)(t−2)3) and satisfyingdimQV =
5.
Example: There are seven cyclic modules whose annihilators contain I, and
thus will vanish by I, enumerated as follows:
V1 := Q[t]/(t − 2), V 2 := Q[t]/((t − 2)2), V 3 := Q[t]/((t − 2)3),
W1 := Q[t]/((t3 − 2)), W 2 := Q[t]/((t3 − 2)(t − 2)),
W3 := Q[t]/((t3 − 2)(t − 2)2), W 4 := Q[t]/((t3 − 2)(t − 2)3);
with dimensions over Q of 1, 2, 3, 3, 4, 5, and 6 respectively. Any product of
these modules will produce a modules annihilated by I, so we need only consider
products that give dimension 5, which are precisely the following:
• V1 ⊕V1 ⊕V1 ⊕V1 ⊕V1,
• V1 ⊕V1 ⊕V1 ⊕V2,
• V1 ⊕V2 ⊕V2,
• V1 ⊕V1 ⊕V3,
• V2 ⊕V3,
• V1 ⊕V1 ⊕W1,
• V2 ⊕W1,
• V1 ⊕W2,
• W3.
□
36 Abelian Groups of order 56 · 75 How many abelian groups are there ofHint: Describe the primary
decomposition. This way
there is an implicit ordering
unlike invariant factors.
order 5 6 · 75?
Example: We know that in a primary decomposition the situation of one prime
does not inﬂuence the other primes. Thus we can count the number of primary
states of the primes 5 and 7 separately, then multiply their states to attain all
possible primary decompositions which uniquely describe an abelian group of
the desired order. For 5 we need only look at the number of distinct partitions
on 6 – it is suﬃcient to insist the order of partition blocks be non-decreasing;
that is, 6 = n1 + · · · +nk and 1 ≤n1 ≤ · · · ≤ nk ≤ 6. Thus we count.
1, 1, 1, 1, 1, 1 1, 1, 1, 1, 2 1, 1, 1, 3 1, 1, 4 1, 5 6.
1, 1, 2, 2 1, 2, 3 3, 3 2, 4
2, 2, 2
In total there are 11 distinct partitions. For the prime 7 we do the same only
now we look at distinct partitions of 5.
1, 1, 1, 1, 1 1, 1, 1, 2 1, 1, 3 1, 4 5
1, 2, 2 2, 3
A total of 7. Therefore the total number of distinct primary decompositions of
56 · 75 is 77; so there are 77 distinct abelian groups of order 5 6 · 75. □

Algebra – James Wilson 83
37 Abelian Groups of order 108 Find the isomorphism class of abelianHint: Use the primary decom-
position of the abelian groups. groups of order 108 having exactly 4 subgroups of order 6.
Example: Groups of the abelian variety are fully classiﬁed as Z- modules, and
thus we need only consider the possible conﬁgurations whose order is 108 = 2 233.
For each element of order 6 we must have at least one component of order 2,
and at least one component of order 3. In each group we can count the elements
of order 2 as 2 i − 1 where i is the number of Z/2k modules in the primary
decomposition, and likewise the elements of order 3 are counted as 3 j − 1 where
j is the number of Z/3k components in the primary decomposition. Thus we
can quickly count the total number of elements of order 6 in each of the possible
groups as follows:
Z/4 ⊕ Z/27, (21 − 1)(31 − 1) = 2;
Z/4 ⊕ Z/3 ⊕ Z/9, (21 − 1)(32 − 1) = 8;
Z/4 ⊕ Z/3 ⊕ Z/3 ⊕ Z/3, (21 − 1)(33 − 1) = 26;
Z/2 ⊕ Z/2 ⊕ Z/27, (22 − 1)(31 − 1) = 6;
Z/2 ⊕ Z/2 ⊕ Z/3 ⊕ Z/9, (22 − 1)(32 − 1) = 24;
Z/2 ⊕ Z/2 ⊕ Z/3 ⊕ Z/3 ⊕ Z/3, (22 − 1)(33 − 1) = 68.
Now as the only abelian group of order 6 is Z/6, and we know ϕ(6) = 2
we know each subgroup of order 6 is precisely one which contains exactly two
elements of order 6. Therefore we need a group with exactly 8 elements of order
6; so our group is isomorphic to Z/4 ⊕ Z/3 ⊕ Z/9. □
38 Noetherian Modules – True or False? If V is a noetherian modules Hint: Consider the chain of
ideals produced by the kernel
of a surjection.
over a ring, then any surjective endomorphism of V is bijective.
Proof: True. Take f : V → →V to be a surjective endomorphism. We may
invoke the ﬁrst isomorphism theorem to state that V/Ker f ∼= V . Now sup-
pose the kernel is non-trivial. Then f −1(Ker f) is a module properly contain-
ing Ker f as Ker f is non-trivial. Call K0 = Ker f and Ki+1 = f −1(Ki).
This gives an ascending chain. Moreover, if Ki = Ki+1 then f −1(Ki) = Ki
for some minimum i. Yet this requires that Ki not properly contain Ki−1
which contradicts the minimality of i (take an element x ∈Ki\Ki−1, certainly
f −1(x) = x+Ki−1 ⁄=Ki−1 asx /∈Ki−1.) So we have an inﬁnite ascending chain
which does not stabilize. So as this conﬂicts with the noetherian assumption it
follows our insistence that K0 ⁄= 0 must be false. So f is injective. □
39 Diagonal Submodules LetV andW be simple left R-modules. Suppose Hint: Consider the example
Z2 ⊕ Z2, then use the third
isomorphism theorem to prove
the observation.
there exists non-zero elements v ∈ V and w ∈ W such that (v,w ) generates a
proper submodule of V ⊕W . Then V ∼=W .
Proof: First we set up the appropriate diagram. Set V ′ = V ⊕ 0 and W ′ =
0 ⊕W with 0 = 0 ⊕ 0. Thus we may write V ′ ∩W ′ = 0 as they are in V ⊕W .
Moreover, letting U = ⟨(v,w )⟩, we know U ∩V ′ = 0 orV ′ as V ′ is simple. If it
isV ′ then as U ⁄=V ⊕W , there is a proper submodule of V ⊕W/V ′ ∼=W . Yet
W is simple so this cannot be. Hence U ∩V ′ = 0. The symmetric argument

84 CHAPTER 3. MODULES
shows that U ∩W ′ = 0 as well. Thus we have the following lattice:
V ⊕W
/d127 /d127 /d127 /d63/d63/d63
V ′
/d63/d63/d63/d63 U W ′
/d127 /d127 /d127 /d127
0
Now we see that in fact V ∼=W as:
W ∼=W ′/0 =W ′/W ′ ∩U ∼=V ⊕W/U
and at the same time
V ∼=V ′/0 =V ′/V ′ ∩U ∼=V ⊕W/U.
□
40 Cyclic Product IfV1 andV2 are non-isomorphic simple R-modules, thenHint: Show any element
avoiding V1 and V2 generates
a subgroup of distinct from
both. Then conclude such a
subgroup cannot be proper.
the R-module V1 ⊕V2 is cyclic.
Proof: Take any (v,w ) ∈ V1 ⊕V2\V1 ∪V2 and consider the submodules U =
⟨(v,w )⟩. If U is a proper submodule then it cannot be V1 or V2 as we know
(v,w ) to be outside of both. As both V1 and V2 are simple modules, using the
third isomorphism theorem we see that V1 ⊕V2/V1 ∼=V2 and V1 ⊕V2/V2 ∼=V1
provingU cannot contain either V1 orV2 and remain proper. Thus we are forced
into the diagram:
V1 ⊕V2
/d127 /d127 /d127 /d63/d63/d63
V1
/d63/d63/d63/d63 U V2
/d127 /d127 /d127 /d127
0
But this creates a problem as we know V1 is not isomorphic to V2; yet, this
diagram tells us that:
V2 ∼=V2/0 =V2/V2 ∩U ∼=V1 ⊕V2/U
and at the same time
V1 ∼=V1/0 =V1/V1 ∩U ∼=V1 ⊕V2/U.
To avoid this contradiction we require that U =V1 ⊕V2 and therefore V2 ⊕V2
is visibly cyclic. □
41 Simple Products If V1 and V2 are non-isomorphic simple R-modulesHint: Use the third isomor-
phism theorem to construct
the lattice.
then V1 ⊕V2 has exactly four submodules: 0 ⊕ 0, V1 ⊕ 0, 0 ⊕V2, V1 ⊕V2.
Proof: Since V1 and V2 are simple they have no non-trivial submodules, and
by the third isomorphism theorem together with the correspondence theorem it
followsV1 ⊕V2/V1 ∼=V2 andV1 ⊕V2/V2 ∼=V1 have no intermediate modules. So
if there is to be a ﬁfth submodule W it must intersect V1 and V2 trivially and
its join with either V1 or V2 will be the entire module. Therefore
V1 ⊕W =V1 ⊕V2 =W ⊕V2.
Now we project along W toV1 and along W toV2 to see: (by the third isomor-
phism theorem)
V1 ∼=V1/V1 ∩W ∼=V1 ⊕W/W ∼=V1 ⊕V2/W ∼=W ⊕V2/W ∼=V2/W ∩V2 ∼=V2.

Algebra – James Wilson 85
Yet we assumed to begin with that V1 and V2 are non-isomorphic, so we have
no other modules. □
42 Module Quotients – True or False? Let V be a left R-module and
V1 ⁄=V2 be maximal submodules. Then V/V 1 ∩V2 ∼=V/V 1 ⊕V/V 2.
Proof: True. We set up the lattice:
V
/d127 /d127 /d127 /d63/d63/d63
V1
/d63/d63/d63 V2
/d127 /d127 /d127
V1 ∩V2
Since V1 and V2 are maximal it follows V/V 1 is simple and so by the third iso-
morphism theorem so is V2/V1 ∩V2. □
43 Indecomposable Modules LetR be a ring and V be an R-module. Set Hint: Show that the sum
of the two non-trivial idempo-
tents is 1, and that both are
zero-divisors.
E :=EndR(V ), the endomorphism ring of V .
(a) If V id the direct sum of two non-trivial R-submodules, show E contains
an idempotent e ⁄= 0, 1.
(b) Suppose that all zero divisors of E lie in a proper ideal J ∈E. Show that
V is indecomposable.
Proof:
(a) Let V =V1 ⊕V2 and deﬁne the endomorphism
e1 :V →V : (v1,v 2) ↦→ (v1, 0).
That this is a well-deﬁned R-linear map is clear. Moreover,
e2
1(v1,v 2) = e1(e1(v1,v 2)) = e1(v1, 0) = (v1, 0) = e1(v1,v 2)
proving that e2
1 =e1 so that e1, and the associated e2 are both non-trivial
idempotents.
(b) First notice that any non-trivial ( ⁄= 0, 1) idempotent is a non-trivial zero-
divisor as e2 =e implies 0 = e2 −e =e(e − 1) and neither e nor e − 1 are
zero. Therefore any idempotents of E are contained in this ideal J.
Now suppose V is decomposable. If V = V1 ⊕V2 ⊕ · · · we may always
take V = V1 ⊕W with W = V2 ⊕ · · · . Now from part (a) we know E has
two distinct idempotents e1 and e2. These must both be contained in J.
Unfortunately,
(e1+e2)(v1,v 2) = e1(v1,v 2)+e2(v1,v 2) = (v1, 0)+(v2, 0) = (v1,v 2) = id(v1,v 2)
proving that 1 = e1 +e2 in E. Therefore J =E. Yet J was assumed to be
a proper ideal so we are forced to accept that V is in fact indecomposable.
□
44 Matrix Subrings – True or False? Let R be a subring of Mn(Q) which Hint: ShowR is torsion-free.
is ﬁnitely generated as a Z-module. Then R is free as a Z-module.

86 CHAPTER 3. MODULES
Proof: True. From the canonical representation of ﬁnitely generated modules
over a PID we know that if R is torsion-free (over Z) then it is indeed free as
a Z-module. Notice that any torsion of R is also torsion in Mn(Q). However
Q is torsion-free over Z and the action of Z on the matrices is component-wise
multiplication so indeed there is no Z-torsion in Mn(Q). □
45 Schur’s Lemma Converse – True or False? If V is a left R-moduleHint: Note that any endo-
morphism from f : Q → Q
is completely determined by
f (1). Thus EndZ(Q) = Q.
and EndR(V ) is a division ring, then V is simple.
Example: False. This demonstrates the converse of Schur’s lemma cannot be
obtained. Consider Q over Z as a module (as an abelian group.) We begin with
a short lemma: given any integral domain R, and two maps f,g :Q(R) →Q(R)
such that f |R =g|R and both R-linear, it follows f =g.3
To prove this we resort to slight of hand:
nf (1/n) = f (n/n) = f (1) = g(1) = g(n/n) = ng(1/n);
(note f (1) = g(1) because they agree on R) therefore, f (1/n) = g(1/n) by the
cancellation property of R. As such,
f (m/n) = mf (1/n) = mg(1/n) = g(m/n).
So f =g.
Now we see we can characterize any R-module endomorphism f : Q(R) →
Q(R) by simply stating what f (1) equals: f (m) = mf (1) so f (1) determines fR
and by our above lemma this is suﬃcient to uniquely determine f . Finally, given
anyθ ∈Q(R), it follows fq(m/n) = m/n ·q is an R-module endomorphism form
Q(R) to Q(R) so indeed EndR(Q(R)) ∼=Q(R) so it is a division ring (ﬁeld.)
Whenever R is not ﬁnite, it follows R ⁄= Q(R), so Q(R) has R as a proper
R-submodule proving Q(R) is not simple. Thus Schur’s lemma may not be im-
proved in this fashion. □
46 Noetherian Modules – True or False? Every ﬁnitely generated moduleHint: Notice that the given
ring is itself noetherian. over R[x,y,z ]/(x2 −y3,y 2 +z2) is noetherian.
Proof: Let R = R[x,y,z ]/(x2 −y3,y 2 +z2). It is suﬃcient to prove that R is
noetherian as any ﬁnitely generated module over a noetherian ring satisﬁes the
ascending chain condition. 4 First not that R a UFD so R[x,y,z ] is as well. So
we can look at irreducible factors. If we brieﬂy pass to C(x,y,z ) we see we can
factor these completely as follows:
x2 −y3 = (x −
√
y3)(x +
√
y3), y 2 +z2 = (y −iz)(y +iz).
However none of these factors are in R[x,y,z ] so we now know they are irre-
ducible and so there are no intermediate ideals proving R is in fact noetherian.
□
47 Zero-Divisors in Group Algebras – True or False? If G is a ﬁniteHint: Consider gn − 1 = 0 .
abelian group then the group algebra QG is a domain.
Example: Let g ∈G, g ⁄= 1 and |g| =n, so that gn = 1. Certainly then
(1 −g)(1 +g +g2 + · · · +gn−1) = 1 −gn = 1 − 1 = 0.
3 When we are willing to allow ring homomorphism to send one to other numbers, then
the statement can be improved to say any ring R, possibly even without a 1, and any ring
homomorphisms f, g : Q(R) → R are completely determined by where they send R.
4From the Hilbert basis theorem this is already clear. R is a quotient of a noetherian ring
so it is noetherian.

Algebra – James Wilson 87
However clearly 1 −g ⁄= 0 and 1+ g +· · ·+gn−1 ⁄= 0 so RG has a zero-divisor. The
converse of this is an open conjecture. □
48 Commutative Semi-simple Rings – True or False? A commutative Hint: Show matrices com-
mute only if they have dimen-
sion 1.
ring is left semi-simple if and only if it is isomorphic to a direct sum of ﬁnitely
many ﬁelds.
Proof: True. A semi-simple ring is isomorphic to a ﬁnite product of matrix
rings over division rings by the Wedderburn-Artin theorem. First of all, as the
division ring is embedded in every matrix ring over the division ring, it follows
for our ring to be commutative that each of the prescribed division rings be
commutative. Furthermore, any non-trivial matrix ring over a ﬁeld remains
non-commutative as it has elements of the form:
A =


0 1 · · ·
1 0
...

 B =


1 0 · · ·
0 0
...


which yield:
AB =


0 0 · · ·
1 0
...

, BA =


0 1 · · ·
0 0
...

,
which clearly are not equal. Therefore the dimension of each matrix must be
1 × 1 and so in fact the ring is simply a ﬁnite product of ﬁelds. □
49 Idempotents and J(R) Prove that J(R) contains no non-zero idempo- Hint: Show any non-trivial
(⁄= 0, 1) idempotent is a zero-
divisor.
tent.
Proof: True. We use the characterization of the Jacobson radical as the set of
allx ∈R such that for any r ∈R, 1 −rx is left invertible. Given any non-trivial
idempotent e ⁄= 0, 1, we quickly see e is a zero-divisor (on the left and right) as
0 = e −e2 =e(1 −e) = (1 −e)e. Therefore 1 −e is not invertible on the left or
right so it is not in the Jacobson radical. Furthermore, 1 /∈J(R) as 1 is not in
any maximal ideal. So the only idempotent in J(R) is 0. □
50 Nilpotent Ideal – True or False? In a ring R the set of nilpotent elements Hint: Consider non-
commutative rings.is an ideal.
Example: False. If R is commutative then it is true and the ideal is precisely
the nil-radical
√
0. However if we take the non-commutative ring M2(Q) we
quickly ﬁnd two nilpotent elements:
A =
[0 1
0 0
]
and B =
[0 0
1 0
]
where A2 = 0 and B2 = 0; yet, A +B a unit (it is a permutation matrix).
Thus if A and B are in a ideal in M2(Q) then this ideal is the entire ring. As
the identity is not nilpotent it is clear such an ideal is not simply composed of
nilpotent elements. □
51 Nilpotency in Semi-simple Rings – True or False? If R is a commu- Hint: The Jacobson radical of
a commutative ring contains
all nilpotent elements.
tative semi-simple ring and r ∈R with r2 = 0 then r = 0.
Proof: True. Given R is semi-simple it follows J(R) = 0. Furthermore, as R
is commutative it contains all nilpotent elements; so r ∈ J(R) = 0. Without

88 CHAPTER 3. MODULES
further question, r = 0. □
52 Semi-simple Rings of order 4 R is a semi-simple ﬁnite ring of order 4.Hint: Use Wedderburn-Artin.
What must R be?
Example: Two possibilities arise immediately: the ﬁeld of order 4 F4 and the
product of the ﬁeld of order 2, F2 ⊕ F2.
Now we prove these. Given R is semi-simple, by the Wedderburn-Artin
theorem it is a product of matrix rings over division rings. As these must be
ﬁnite, so must the division ring. Indeed by the little theorem of Wedderburn,
every ﬁnite division ring is a ﬁeld. The smallest non-trivial matrix ring M2(F2)
already has 16 elements, so in fact our ring a product of ﬁelds. Therefore it can
only be F2 ⊕ F2 or F4. □
53 Jacobson Radical – True or False? For every left noetherian ring R,Hint: Consider a local ring.
the Jacobson radical J(R) is the largest nilpotent ideal of R.
Example: False. When R is artinian this is true. However when we take a
noetherian non-artinian local ring such as C[[x]] we see we get J(C[[x]]) = (x) –
the unique maximal ideal (left/right do not matter as we have a commutative
ring).5 However (x) is not a nilpotent ideal. Notice ( x)n = (xn) ⁄= 0 for any
n ∈ Z+. □
54 Semi-simple Rings – True or False? If R is a noetherian commutativeHint: Consider the integers.
ring then R/J (R) is a semi-simple ring (i.e.: every R-module is semi-simple).
Example: False. Let R = Z. Z is noetherian and any chain of ideals begin-
ning with 0 must next go to mZ for some m. From here there are only ﬁnitely
many ideals until Z is reached. Also, the maximal ideal of Z are pZ where p is
prime. So the intersection is the set of all integers which every prime divides; so
J(R) = 0. Hence R/J (R) ∼= R. Yet Z is not semi-simple as it is not artinian:
evidenced by (1) > (2)> (4)> (8)> · · ·. □
55 Jacobson Radical of Z/m Calculate the Jacobson radical of the ringHint: Maximal ideal in Z cor-
respond to primes. Z/mZ.
Example: Since prime ideals are maximal in a PID, we have pZ as the maximal
ideals of Z wherep is prime. Thus when we consider Z/mZ, the maximal ideals
are pZ/mZ where p|m (if (p,m ) = 1 then mZ is not a subring of pZ, so it
is not included in the quotient lattice.) Now their intersection follows their
intersection in Z: pZ ∩qQ = [p,q ]Z, where [ p,q ] is the least common multiple
of p and q; hence, the intersection of maximal ideals in Z/mZ is:
[p1,...,p n]Z/mZ, p |m.
A ﬁnal cosmetic step is to observe that kZ/mZ ∼= Z/(m/k)Z where k|m (as
otherwise the quotient is not deﬁned.) So we may write:
J(Z/mZ) ∼= Z/GCDp|m
(m
p
)
Z.
□
56 Idempotents and Jacobson Radicals Let e ∈ R be a non-zero idem-Hint:
5C[[x]] is noetherian by the Hilbert basis theorem, and not artinian by the obvious de-
scending chain ( x) > (x2) > (x3) > · · · .

Algebra – James Wilson 89
potent. Then eRe is a ring and J(eRe) = J(R) ∩eRe.
Proof: Givena,b ∈R, notice eae +ebe =e(a +b)e ∈eRe. Also notice
eae +e(−a)e =e(a −a)e =e0e = 0
so e(−a)e = −eae and thus R contains inverses, and clearly also 0 so it is non-
empty and thus a subgroup of R under addition. Also notice ( eae)(ebe) =
eaeebe = e(aeb)e which is in R and so eRe is closed under multiplication;
moreover, the multiplication is associative since it is also in R. For unity we
takee, and notice that indeed:
(eae)(e) = eae =e(eae).
Hence, eRe is a unital ring. 6
Now consider a simple left R-module V . We may take eV and all the prop-
erties for eRe-modules hold, with the only interesting feature being the unital
nature:
e(ev) = eev =ev.
So we have eV as an eRe-module, although possibly trivial. Thus the annihi-
lators of simple eRe-modules in eRe are a subcollection of the annihilators of
simple R-modules, intersected with eRe. So J(eRe) ⊆ J(R) ∩eRe. PEND-
ING: reverse inclusion □
57 Jacobson Radical of Matrices LetR be a ring. Show that J(Mn(R)) = Hint:
Mn(J(R)).
Remark 3.0.9 The following proof is a farce. Our recent examples over Z show
that left ideals such as:
M2(Z) ·
(1 5
0 7
)
.
are maximal and yet clearly not contained in any of the proposed maximal ma-
trices in the proof. These may in fact not be maximal, but certainly are not
suﬃcient.
Proof: Let {Ji : i ∈ I} be the maximal left ideals of R. First we claim the
maximal left ideal of Mn(R) are the sets
mk(Ji) = {(ai,j ∈Mn(R) : ai,k ∈Ji}
for all i ∈ I and all k = 1,...,n . Since each Ji is closed to sums and absorbs
products on the left, it follows each mk(Ji) is a left ideal of Mn(R). Furthermore,
as eachJi is maximal in R, we cannot adjoin any other matrices without forcing
the k-th column to contain all elements of R, and thus obtain Mn(R); hence,
eachmk(Ji) is maximal in Mn(R).
Now suppose M is a maximal left ideal of Mn(R). It follows then we may
express M = (Ii,j) where Ii,j are each left ideals of R. Moreover, as we can
multiply on the left by permutation matrices – an action that can resort rows –
we must have each column with the same ideal; that is, Ii,k =Ij,k for all i,j and
k. Now to be proper, we must have some column ideal Ii,k be a proper ideal
in R. To remain maximal we require that only one column have this, and that
this column’s ideal be maximal in R. Hence the maximal left ideal in Mn(R)
are in fact exactly all mk(Ji).
6Even when R itself it not unital we have this situation; however, when R has unity 1,
then e = e1e as expected.

90 CHAPTER 3. MODULES
Now intersect these maximal ideals and we see as i ranges that each column
space must have entries over the intersection of all maximal left ideals – J(R).
Furthermore, lettingk range we see each column must be over J(R), and so the
matrices themselves are exactly those of Mn(J(R)). □
58 Nakayama’s Lemma Let V be a ﬁnitely generated left R-module, andHint: Use Nakayama’s
Lemma. π : V → V/J (R)V be the projection. If π(v1),...,π (vn) generate V/J (R)V ,
then v1,...,v n generate V .
Proof: LetW be the span of v1,...,v n and as required assume W +J(R)V =V
since π(v1),...,π (vn) generates V/J (R)V (this is not assuming what is to be
proved, it is simply writing the same details as cosets.) Thus by Nakayama’s
Lemma we have W =V , so indeed the vectors span V . □
59 Jacobson Radical – True or False? J(R1 ⊕ · · · ⊕Rn) = J(R1) ⊕ · · · ⊕Hint: Use the result of
Exercise-3.56 to determine the
internal direct product.
J(Rn).
Proof: True. We saw in Exercise- 3.56 that given a non-trivial idempotent
e, eRe formed a ring and furthermore J(eRe) = J(R) ∩eRe. Now take the
idempotents e1 = (1, 0, · · ·, 0) through en = (0,..., 0, 1) in R =R1 ⊕ · · · ⊕Rn.
It follows that eiRei ∼=Ri. Also,
J(R) ∩eiRei =J(eiRei) ∼=J(Ri).
As such we see that
J(eiRei) ∩J(ejRej) = 0
wheneveri ⁄=j. Also clearly
J(R) = J(e1Re1) + · · · +J(enRen).
Therefore we have the ingredients for an internal direct product:
J(R1) ⊕ · · · ⊕J(Rn) ∼= J(e1Re1) ⊕ · · · ⊕J(enRen)
= J(e1Re1 ⊕ · · · ⊕enRen)
= J(R1 ⊕ · · · ⊕Rn).
□
60 Jacobson Radicals of PIDs LetF be a ﬁeld and R =F [x]/I whereI isHint: ExpressR in its primary
decomposition. the ideal of F [x] generated by x2 + 2x + 1. What is the Jacobson radical of R?
Example: Notice ﬁrst that x2 + 2x + 1 = ( x + 1) 2 and x + 1 is irreducible.
As F [x] is a PID it follows irreducible elements generate maximal ideals. Since
we have a commutative ring we care only about full ideals, not left. Further-
more, I = ((x + 1)2) is ( x + 1)-primary so our quotient ring has precisely one
maximal ideal, namely ( x + 1)/((x + 1)2). Therefore the Jacobson Radical is
(x + 1)/((x + 1)2). □
61 Nakayama’s Lemma Prove the following generalization of Nakayama’sHint: Use Nakayama’s
Lemma. Lemma. If R is an arbitrary ring, I a two-sided ideal of R contained in the
Jacobson Radical of R, and V a left ﬁnitely generated R-module such that
IV =V , then V = 0.
Proof: Since I is contained in J(R), it follows J(R)V ≥ IV = V , and so
J(R)V =V . However Nakayama’s lemma tells us that 0 + J(R)V =V implies
V = 0, so we are done. □

Algebra – James Wilson 91
62 Schur’s Lemma – True or False? If V is an irreducible R-module, theHint: Use Schur’s Lemma
center of EndR(V ) is a ﬁeld.
Proof: True. By Schur’s Lemma we recognize the EndR(V ) is a division ring.
The center of a division ring is a commutative division ring and so it is a ﬁeld. □
63 Semi-simple Rings Say what you can about an artinian ring containing Hint: Consider nilpotent ide-
als ﬁrst.no non-zero nilpotent elements.
Example: Given any nilpotent ideal, all its elements are nilpotent. Thus,
each nilpotent ideal is trivial. Moreover, the Jacobson radical is the maximal
nilpotent ideal since our ring is artinian; so it must, therefore, be trivial. As our
ring is artinian and has trivial Jacobson radical, we now see it is a semi-simple
ring.
As any semi-simple ring is artinian and has trivial Jacobson radical, (and
consequently no non-zero nilpotent elements) this statement cannot be im-
proved. □
64 Division Rings – True or False? If R is a left artinian ring containing Hint: Use the Wedderburn-
Artin theorem.no zero-divisors, then R is a division ring.
Proof: True. As R has no zero-divisors it has no nilpotent elements, and thus
also no nilpotent ideals. Hence the Jacobson radical is trivial as in an artinian
ring it is always nilpotent; therefore, R is semi-simple artinian. Making use of
the Wedderburn-Artin theorem we now see
R ∼=Mn1(D1) ⊕ · · · ⊕Mnk (Dk).
However if any ni > 1 then there are zero-divisors, for example:
A =


· · · 0 1
0
...


is nilpotent so it is a zero-divisor. Hence
R =D1 ⊕ · · · ⊕Dk.
Yet even this is a problem as we have idempotents (for example (1 , 0,..., 0))
which are not 0 or 1, and such elements are always zero-divisors. 7 We are left
with the conclusion
R =D1
where D1 is a division ring. □
65 Division Algebras – True or False? Let F be a ﬁeld. A ﬁnite Hint: Show A is left artinian
then use Exercise- 3.64.dimensional F -algebra without zero-divisors is a division algebra.
Proof: True. Let A be a ﬁnite dimensional F -algebra with no zero-divisors.
Given any left ideal I in A, it follows I is an F -subspace of FA. Take a chain
of descending left ideals I0 ≥I1 ≥ · · · in A. It follows with it we get
dimFA ≥dimFI0 ≥dimFI1 ≥ · · · .
YetF is a ﬁeld so if dimFIi =dimFIi+1 thenIi =Ii+1. As the total dimension
of A as an F -vector space is ﬁnite it follows the descending chain stabilizes in
7e(1 − e) = 0, e ⁄= 0, 1 − e ⁄= 0.

92 CHAPTER 3. MODULES
ﬁnitely many steps; hence, A is left-artinian. As A has no zero-divisors, as we
saw in Exercise- 3.64, it is semi-simple and consequently also a division ring, our
in our case a division algebra. □
66 Simple Artinian Rings – True or False? If a ring R is simple artinianHint: Every simple artinian
ring is isomorphic to a ring of
matrices over a division ring.
then the ring of all 2 × 2 matrices over R is simple artinian.
Proof: True. As the Jacobson radical is a two-sided ideal, in R it must be
trivial. As R is also artinian it follows it is in fact semi-simple artinian. So by
the Wedderburn-Artin theorem we know
R ∼=Mn1(D1) ⊕ · · · ⊕Mnk (Dk).
Yet unless k = 1, there are two sided ideals in this presentation (we see this
by the projection map π1 which has as its kernel the ideal Mn2(D2) ⊕ · · · ⊕
Mnk (Dk).) Therefore R = Mn(D). There is an obvious isomorphism between
M2(Mn(D)) and M2n(D); therefore, it is simple artinian as matrix rings over
division rings are always simple artinian. □
67 Group Algebras Let G be a ﬁnite group and F be an algebraicallyHint: Show FG/J (FG ) is
semi-simple artinian. closed ﬁeld of characteristic p. Prove the following:
(i) Up to isomorphism, that there are only ﬁnitely many irreducible FG -
modules L1,...,L k.
(ii) Let di =dim Li, 1 ≤i ≤k. Then ∑k
i=1d2
i ≤ |G|, and the equality holds
if and only if p ∤ |G|.
(iii) Is it true that the inequality ∑k
i=1d2
i ≤ |G| holds even if F is not alge-
braically closed?
Proof: Since any ﬁeld F is commutative, left ideals are in fact ideals and so
F has no proper left ideals. Hence F is trivially artinian. Since G is ﬁnite, and
FG is a ﬁnite dimensional F vector space (hence FG ∼= F × · · ·F over F ) it
follows FG is artinian. Consider the Jacobson radical J = J(FG ), [which is
trivial when char F does not divides the order of G – Maschke’s Theorem.]
Study FG/J . As J is an ideal of FG , this quotient is a well-deﬁned ring.
Moreover, as quotients of artinian rings are artinian, and J(FG/J ) = 0, we
now see FG/J is semi-simple artinian. We now may consider any simple left
FG/J module V . Since J annihilates all simple FG modules, we may inﬂate
V to and FG -module, and for the same reason we may go back. Thus there is
a one to one correspondence between the simple FG -modules and the simple
FG/J -modules.
We may now answer the ﬁrst problem: FG/J is semi-simple artinian, so it
has ﬁnitely many irreducibles – make use here of the Wedderburn-Artin repre-
sentation of semi-simple rings.
The second result follows from that fact that our modules are inﬂated to
FG -modules. Clearly from the Wedderburn-Artin theorem, the modules over
FG/J have the property that ∑k
i=1d2
i = |G|. However, over a larger ring,
the dimensions are possibly less. Using Maschke’s theorem, the equality holds
wheneverp does not divide the order of G.
Finally for the third question is false. For example, given C3, we may use Q
and study QC3. For notational convenience let C3 be generated by a primitive
3rd root of unit ω.
It follows e = 1 + ω +ω2 is an idempotent. Its associated principal ideal
QC3e = Qe is simple as it is isomorphic to Q. We also immediately see QC3 =

Algebra – James Wilson 93
Qe ⊕ QC3(1 −e). We also notice that QC3(1 −e) = Q(ω). Hence as it is a ﬁeld
it too is simple. So we have our simple decomposition:
QC3 = Q(1 +ω +ω2) ⊕ Q(ω)
and as dimQQ(ω) = 2 and clearly 1 1 + 22 > 3. □
68 Group Algebras Let Cn be the cyclic group of order n. Decompose the Hint:
group algebra CCn as a direct sum of simple ideals. Do the same for QCn.
Example: LetF be either Q or C. Let Cn = ⟨ω⟩ where for convenience ω ∈ C
is a primitive n-th root of unity when F = Q and simply an abstract generator
outside of C whenF = C. The element e = 1 +ω + · · · +ωn−1 lies in FCn and
furthermore, the left ideal L1 =FCne =Fe so dimFL1 = 1. This means L1 is
an irreducible FCn-module as any smaller module would have dimension 0.
It also follows that e2 = e so we see that FC nFCn = FCne ⊕FCn(1 −e).
Now we need to decompose FCn(1 −e). Notice what elements look like here:
n−1∑
i=0
aiωi · (−ω −ω2 − · · · −ωn−1) = −
n−1∑
k=1
n−1∑
i=0
aiωi+k.
So let a0 = −1 and ai = 0 for all i >0. Then the result is simply ω. Hence,
F (ω) ≤FCn(1 −e).
One ﬁnal general property is to note that each left ideal of FCn is an F -
vector space. Add to this the fact that FCn is semi-simple artinian by Maschke’s
theorem and it is commutative so we know it is a product of ﬁelds. Hence the
decomposition must have the following property:
FCn ∼=F1 ⊕ · · · ⊕Fk
where dimFF1 + · · · +dimFFk =dimFFG = |G|.
Now we make use of the speciﬁc ﬁelds.
When F = Q it follows F (ω) = Q(ω), and 2 = dimQQ(ω) ≤dimQQCn ≤ 2.
Therefore QCn(1 −e) = Q(ω) and as such it is a ﬁeld so we have satisﬁed the
Wedderburn-Artin claim and as such we know L2 = QCn(1−e) to be irreducible
and ﬁnally that
QCn = Qe ⊕ QCn(1 −e) ∼= Q ⊕ Q(ω).
When F = C the result is little diﬀerent. The fact that all ﬁnite dimension
ﬁeld extensions of C are of degree 1 forces us to admit dimCFi = 1 for all i
and so there are L2 through Ln all isomorphic to C. Now we must ﬁnd their
generators by decomposing CCn(1 −e). □
69 Commutative Algebras – True or False? LetA be a ﬁnite dimensional Hint: Use The Jacobson Den-
sity Theorem together with
Schur’s Lemma.
commutative algebra over an algebraically closed ﬁeld F . Then all simple A-
modules are 1 dimensional over F .
Proof: True. The proof is a trail of falling dominoes. Let V be a simple
A-module. From Schur’s lemma it follows EndA(V ) is the ﬁeld F , since F is
algebraically closed, V is simple, and A is an F -algebra. Now as A is ﬁnite
dimensional over F , we know any quotient by a left ideal is also ﬁnite dimen-
sional, and in particular our simple module V , which is isomorphic to one such
quotient, must be ﬁnite dimensional as an F vector space.
Now we consider EndF (V ) which is all F -linear maps from V to V and
hence completely determined by a ﬁnite basis {e1,...,e n}. However, V is simple
and each of its two submodules has each other as a complement so V is semi-
simple. Hence we may invoke the Jacobson Density Theorem to infer that to

94 CHAPTER 3. MODULES
any f ∈ EndF (V ) there exists an r ∈ A such that f (ei) = rei. Since F is
central in A it follows:
f (⃗ x) = f (a1e1 + · · ·anen) = ra1e1 + · · ·ranen =r⃗ x
where ai ∈ F , and ⃗ x∈ V as an F vector space. Therefore f is completely
characterized by left translation, and as any r produces a viable F -linear endo-
morphism of V , we now see there exists a surjective ring epimorphism form A
ontoEndF (V ).8
Finally we observe the EndF (V ), being simply linear transformations of a ﬁ-
nite dimensional vector space, must coincide with Mn(F ). However this requires
A map surjectively as a ring onto Mn(F ). Since A is given as a commutative
ring, it follows Mn(F ) must also be commutative, which requires n = 1. Thus
V is 1-dimensional over F . □
70 Commutative Algebras – True or False? Let A be a ﬁnite dimen-Hint: Consider QC4.
sional commutative algebra over a ﬁeld F . Then all simple A-modules are 1
dimensional over F .
Example: False. Consider QC4. In Exercise- 3.68 we saw that
QC4 ∼= Q ⊕ Q(ω)
where ω is a primitive fourth root of unity. As dimQQ(ω) = 3 we see it is not
of dimension 1. □
71 Simple Modules over Algebras Let A be a ﬁnite dimensional algebraHint: Use the Jacobson Den-
sity Theorem. over an algebraically closed ﬁeld F , and V be simple A-module.
(i) Show that V is ﬁnite dimensional.
(ii) Let {v1,...,v n} be a basis of V , and π(b) be a matrix of a linear trans-
formation V → V , v ↦→ bv with respect to this basis. Show that for any
matrix B ∈Mn(F ) there exists b ∈B with B =π(b).
(iii) Show that (ii) may fail if F is not algebraically closed.
Proof: CertainlyV is a quotient of A, so it is an F vector space. Moreover, V
has ﬁnite dimension over F as A has ﬁnite dimension, and quotients of vector
spaces have dimensions less than or equal to the original. Now assume v1,...,v n
is a basis of V overF . As Schur’s lemma applies, we know the endomorphisms of
V overA are simply F . Moreover, now the Jacobson Density Theorem applies,
since simple modules are semi-simple, so we get that EndF (V ) is characterized
completely by scalar transformations given a ﬁnite number of vectors. Yet we
have a ﬁniteF dimensional space so we have indeed all our transforms are scalar.
Thus, as EndF (V ) = Mn(F ) we see to every matrix B ofMn(F ) there exists a
scalar b such that B =π(b). □
Example: For the counter-example let F = R and consider V =C C as an
R-algebra. As dimRC = 2 we see that indeed C is a ﬁnite dimensional algebra
8
fr(s⃗ x+ ⃗ y) = rs⃗ x+ r⃗ y= sfr(⃗ x) + fr(⃗ y);
(fr + fs)(⃗ x) = r⃗ x+ s⃗ x= (r + s)⃗ x= fr+s(⃗ x),
fr ◦ fs(⃗ x) = rs⃗ x= frs(⃗ x).

Algebra – James Wilson 95
over R. Clearly V is a simple C-module as C has no proper ideals. The matrix
corresponding to complex conjugation, namely
[1 0
0 −1
]
is not scalar. □
72 Finite Rings A ﬁnite ring with no nilpotent elements is a direct product Hint: Use the Wedderburn-
Artin theorem.of ﬁelds.
Proof: Given a ﬁnite ring R, it can have only ﬁnitely many subsets and so also
only ﬁnitely many left ideals. Hence it is left artinian. As such, the Jacobson
radical is a nilpotent ideal, and so every element of J(R) is nilpotent. Since we
also assume R has no nilpotent elements it is clear that J(R) = 0. Thus R is
semi-simple artinian. By the theorem of Wedderburn-Artin we know
R ∼=Mn1(D1) ⊕ · · · ⊕Mnk (Dk).
Yet as seen many times before, every matrix ring with n> 1 has nilpotent ele-
ments so each ni = 1. Moreover by the little theorem of Wedderburn we know
each ﬁnite division ring is a ﬁeld, so we are left with the conclusion that R is a
direct product of ﬁelds. □
73 Finite Simple Rings Describe the ﬁnite simple rings. Hint: Use Wedderburn-Artin
and the little Wedderburn the-
orem.
Example: Every ﬁnite ring is trivially left artinian. Moreover, as R is simple,
it has only one maximal two-sided ideal – the trivial ideal – so J(R) = 0 as it
is a two-sided ideal and must be contained in a maximal ideal. Thus R is left
semi-simple. Therefore R is simple and semi-simple then by Theorem-3.11.13
we know R ∼= Mn(D) for some division ring D. Furthermore, D is embedded
in Mn(D) which must be ﬁnite, so it is a ﬁnite division ring and hence by the
little Wedderburn theorem, D is a ﬁeld. Finally we can say R ∼= Mn(F ) for
some ﬁnite ﬁeld F .
Now, given any ﬁnite ﬁeld Fpk , we know from Thm-3.11.13 that Mn(Fpk )
is simple. Moreover, for each n it is also ﬁnite, so the description cannot be
improved as each Mn(Fpk ) is a viable simple ﬁnite ring.
It may be of interest to note that each ﬁnite simple ring has order pkn2
and
for each pm there are exactly as many simple rings as there are ways to write
m = kn2. In particular, there is only a unique simple ring (the ﬁeld) of order
pq where p and q are prime. □
74 Complex Algebra Dimensions – True or False? If A is a ﬁnite Hint: Use the Wedderburn-
Artin theorem.dimensional simple algebra over C, then dimC A is a perfect square.
Proof: True. Since A is a ﬁnite dimensional C-algebra, it follows any de-
scending chain of left ideals must have distinct dimensions over C for each step.
Being ﬁnite dimensional over all, all such chains must stabilize in ﬁnitely many
steps. Thus A is left artinian. Moreover, A is simple so its Jacobson radical is
trivial as J(A) is a two-sided ideal. Therefore A is semi-simple artinian and so
we invoke the Wedderburn-Artin Theorem to state:
A ∼=Mn1(D1) ⊕ · · · ⊕Mnk (Dk)
for division rings Di.

96 CHAPTER 3. MODULES
Finally we have proper two-sided ideals Mni(Di) if k ⁄= 1. So since A is
simple we require k = 1. Thus indeed
A ∼=Mn(D).
As such, dimC A = dimC Mn(D) = ( dimC D)2 so the dimension is a perfect
square.
One ﬁnal problem is if n = 1 and so dimC A = dimC D. However such a
division ring is a division C-algebra and is also ﬁnite dimensional. We will show
this requires C =D since C is algebraically closed.
Given any ﬁnite dimensional ﬁeld of extension is algebraic, there are only
trivial ﬁnite dimensional ﬁeld extensions of C. Also, C is in the center of D.
Now takea ∈D. It follows for any x ∈ C thatax =xa so indeed C(a) is a ﬁeld.
Yet C(a)/C is a ﬁnite ﬁeld extension and so C(a) = C. In conclusion D = C. □
75 Division Rings Let R be a ring and J be its Jacobson Radical. ThenHint: Use the correspondence
theorem on some maximal left
ideal properly containing J.
R/J is a division ring if and only if R has a unique maximal left ideal.
Lemma 3.0.10 A ring R with identity 1 ⁄= 0 is a division ring if and only if
R has no proper left ideals.
Proof: Consider R, a unital ring. When R is a division ring and I a left ideal
of R, I must absorb product. But for all r ∈I, if r ⁄= 0 then there exists a left
inverser′ such that r′r = 1. Therefore when I is nonzero it is the entire ring.
So R has no proper left ideals.
ConsiderR to be a unital ring with no proper left ideals. Given any nonzero
element a in R, which must exists since 1 ⁄= 0, then Ra is a left ideal. Left
ideals may not be proper so Ra is 0 or R. The unity of R allowsa ∈Ra where
a ⁄= 0 so Ra =R. Thus 1 ∈Ra so there exists an a′ such that 1 = a′a, so a is
left invertible.
Having shown Ra = R for all nonzero a in R take a and b to be non-zero
elements in R and suppose they are zero-divisors so that ab = 0. Thus it would
follow that 0 = R0 = Rab = (Ra)b =Rb =R but 1 ⁄= 0, forcing R ⁄= 0 so a and
b are not zero-divisors. Therefore R − {0} is closed under multiplication and so
it is a semigroup with left identity and left inverses so it has a multiplicative
group structure. Therefore R is a division ring. □
Now to the exercise. Proof: Suppose J is not a maximal left ideal – that is
the same as suppose there are more than one such ideals. Then J is properly
contained in any maximal left ideal, say for instance M . As such R/J has
a proper left ideal M/J by the correspondence theorem; hence, R/J is not a
division ring. So by the contrapositive, if R/J is a division ring then R has
exactly one maximal left ideal.
IfR has a unique maximal left ideal then it is precisely the Jacobson radial.
Also as J is maximal it follows R/J has no proper left ideals. Since R/J has an
identity and no proper left ideals it follows it is a division ring. We prove this
with as a lemma. □
76 Division Rings – True or False? IfR is a semi-simple artinian ring withHint: Consider Z2 ⊕ Z2.
r3 =r for all r ∈R, then R is a division ring.
Example: False. Notice if r3 =r for all r then 0 = r(r2 − 1) for all r. If r ⁄= 0
and r2 ⁄= 1, then r is a zero-divisor in which case R would not be a division
ring. This means everything must have order 2.
Now we simply look for a semi-simple ring without this property. For in-
stance, Z2 ⊕ Z2 is semi-simple artinian as it is a product of ﬁelds. Moreover

Algebra – James Wilson 97
(a,b )3 = (a3,b 3) = (a,b ). Yet clearly Z2 ⊕ Z2 under componentwise multiplica-
tion is not a ﬁeld or a division ring as it has zero-divisors: (1 , 0)·(0, 1) = (0, 0). □
77 Complex dimension 4 Algebras – True or False? If A and B are Hint: Use the Wedderburn-
Artin theorem to describe the
possibilities.
semi-simple artinian complex algebras of dimension 4 then A ∼=B.
Example: False. By the Wedderburn-Artin theorem we know R = C⊕C⊕C⊕C
andS =M2(C) are complex semi-simple artinian algebras. However R has non-
trivial two sided ideals while S is a simple ring. Therefore R is not congruent
to S. □
78 Complex dimension 3 Algebras – True or False? If A and B are Hint: Use the Wedderburn-
Artin theorem to describe the
possibilities.
semi-simple artinian complex algebras of dimension 3 then A ∼=B.
Proof: True. By the Wedderburn-Artin theorem we know that any complex
dimension 3 algebra must decompose as follows:
A ∼=Mn1(D1)⊕· · ·⊕Mnk (Dk), n 2
1dimCD1 +· · ·+n2
kdimCDk =dimCA = 3.
As no perfect square is less than 3, save 1, it follows each ni = 1. Now recall from
Exercise-3.74 that any ﬁnite dimensional simple algebra over C has a perfect
square for its dimension. Since neither 2 nor 3 are perfect squares there are no
division rings over dimension 2 or 3 over C. It follows the rings take the form
C ⊕ C ⊕ C
and so they are all isomorphic. □
79 Rings of idempotents If R is a left semi-simple artinian ring with Hint: Notice that all non-
zero non-unital idempotents
are zero-divisors.
r2 =r for all r ∈R thenR is isomorphic to a direct product of of copies of F2.
Proof: Since R is semi-simple artinian by the Wedderburn-Artin it takes the
form
R ∼=Mn1(D1) ⊕ · · · ⊕Mnk (Dk).
If any ni > 1 then there exists non-trivial nilpotent matrices which clearly are
not idempotent. So we restrict ourselves to having ni = 1 for each i.
Next suppose 1 < |Di| = n ⁄= 2. Then pick and r ∈ Di which is not 0 or
1. Clearly the fact that r2 =r implies 0 = r(1 −r) proving r is a zero-divisor.
Hence |Di| = 2. As such it is precisely the ﬁeld F2. In conclusion, R is a ﬁnite
direct sum of F2’s. □
80 Nilpotent Free Rings – True or False? If R is an artinian ring having Hint: Consider any non-
commutative division ring.no non-zero nilpotent elements then R is a direct sum of ﬁelds.
Example: False. Take any division ring, for instance the Hamiltonians . As ×
there can be no non-zero zero-divisors, let alone nilpotent elements. As every
division ring has no proper left ideals it is trivially artinian as well. Furthermore,
division rings are simple rings so they cannot be isomorphic to any non-trivial
ring product. As itself is not a ﬁeld we see indeed the claim is false. □
81 Real Algebras of Dimension 2 Classify all 2-dimensional R-algebras. Hint: When the Jacobson
radical is not trivial the alge-
bra is R[x]/(x2). Do not for-
get to show there are no divi-
sion rings of dimension 2 over
R which are not C.
Proof: Let A be a 2-dimensional R-algebra.
As R is a ﬁeld it follows any ﬁnite dimensional R algebra is artinian. If the
Jacobson radical is non-trivial then to be proper it must have dimension 1 over
R. As A is also artinian it follows J(A) is nilpotent and so indeed J(A)2 = 0.

98 CHAPTER 3. MODULES
Select a basis that extends 1, so {1,α }. It follows every element takes the
form a1 +a2α. So consider α2 =a0 +a1α.
If a0 = 0 and a1 = 0. Then α2 = 0 in which case there is a natural
surjection from R[x]/(x2) onto A by sending x ↦→ α. With little eﬀort this is
seen as injective as well. This is the case when there is not a trivial Jacobson
radical.
Now consider a1 ⁄= 0. Suppose b0 +b1α is a nilpotent element of order 2.
0 = ( b0 +b1α)2
= b2
0 + 2b0b1 +b2
1α2
= ( b2
0 +b2
1a0) + (2b0b1 +b2
1a1)α.
Since {1,α } is a basis it follows
b2
0 +b2
1a0 = 0, 2b0b1 +b2
1a1 = 0.
In the ﬁrst we see b2
0 = −b2
1a0, and so a0 must be a square as well. However
in R all squares are non-negative so 0 ≤b2
0 = −(b1
√a0)2. The problem is that
(b1
√a0)2 ≥ 0 as well. Therefore 0 = b0 and either b1 = 0 or a0 = 0. If it is
the former we are done, if it is the latter we return to 2 b0b1 +b2
1a1 = 0 and
notice we need only ask when b2
1a1 = 0. Since we assumed a1 ⁄= 0 we see indeed
b1 = 0. Therefore all nilpotent elements of order 2 are trivial. Hence J(A) = 0.
In the other case that J(A) = 0, it follows A is semi-simple artinian. Hence
A ∼= R ⊕ R, A ∼= C, A ∼=D
where D is some division ring of dimension 2 over R. It remains to show that
any dimension 2 division ring over R is isomorphic to C.
Given {1,α } as a basis of D over R consider the product rα for any r ∈ R.
Since R is in the center of D it follows rα = αr. Now take any two elements
(a +bα), (c +dα) ∈D.
(a+bα)(c+dα) = ac+adα+bαc+bαdα =ca+bcα+dαa+dαbα = (c+dα)(a+bα).
Thus any 2-dimensional division algebra over R is a ﬁeld. As such it is C.
So the list of 2-dimensional R-algebras up to isomorphism is:
R[x]/(x2), R ⊕ R, C.
□
82 Similar Matrices Determine whether or not the matricesHint: Determine the compan-
ion matrices.
A =


1 3 1
2 2 −1
1 1 1

 and B =


0 0 −6
1 0 1
0 1 4


are similar over rationals.
Example: Since Q is not algebraically closed it is possible that some of the
eigenvalues are not in Q and as such we may not use the Jordan Canonical form.
Instead we use invariant factors and the rational canonical form.
First we ﬁnd the characteristic polynomial to be
χA(λ) = λ3 − 4λ2 −λ + 6, χ B(λ) = λ3 − 4λ2 −λ + 6.
Notice in fact B is the companion matrix of χA and χB.

Algebra – James Wilson 99
By the rational root test there are no rational roots so we know χA is irre-
ducible and so the minimal polynomial must equal χA. Hence A is similar only
to matrices whose companion matrix is precisely the same as C(χA). As noted
above,B is such a matrix. So A and B are similar. □
83 Similar Matrices Determine whether or not the matrices Hint: Determine the compan-
ion matrices.
A =


0 1 0
0 0 1
−1 2 1

 and B =


0 1 0
2 3 0
0 0 −5


are similar over rationals.
Example: Since Q is not algebraically closed it is possible that some of the
eigenvalues are not in Q and as such we may not use the Jordan Canonical form.
Instead we use invariant factors and the rational canonical form.
Notice that AT is a companion matrix for p(x) = x3 −x2 − 2x + 1. As A
is similar to AT it follows are have the invariant factors of A. For B we simply
compute it directly as:
χB(x) = (x + 5)(x2 − 3x − 2).
By the rational roots test we ﬁnd p(x) to be irreducible over Q so it is the lone
invariant factor. As χB(x) is reducible, so is the minimal polynomial and so
indeed A and B do not have the same invariant factors. Hence they are not
similar. (Indeed the minimal polynomial for B is χB.) □
84 Nilpotent Matrices An n ×n nilpotent matrix with entries in a ﬁeld Hint: Find the minimal poly-
nomial of nilpotent matrix.has characteristic polynomial xn.
Proof: Take a nilpotent n ×n matrix A. Assume that Ak = 0 for some the
least k. It follows xk is the minimal polynomial for A. As such xk divides the
characteristic polynomial. But we also know that all the roots of the charac-
teristic polynomial are roots of the minimal polynomial, so there can only be 0
eigenvalues. Hence, xn is the characteristic polynomial. □
85 Similarity Classes – True or False? There are exactly 3 similarity Hint: Consider invariant fac-
tors.classes of 4 × 4 matrices A over F2 satisfying A2 = 1.
Example: True. We see that the minimal polynomial of A must divide x2 − 1.
Over F2 this allows for the following factors two factors:
x − 1, x 2 − 1.
Therefore we have the following choices of invariant factors:
x − 1|x − 1|x − 1|x − 1, x − 1|x − 1|x2 − 1, x 2 − 1|x2 − 1.
As invariant factors uniquely describe each similarity class we see we have only
3 similarity classes with the property that the matrices by 4 ×4 and the minimal
polynomial divide x2 − 1. □
86 Similarity Class of F2 Give a list of 2 × 2 matrices over F2 such that Hint: Consider all possible
minimal polynomials and then
from these all possible invari-
ant factors.
every 2 × 2 matrix over F2 is similar to exactly one on your list.
Example: Over F2 the number of polynomials of degree 2 or less is few and
each is allowed as a minimal polynomial of 2 × 2 matrices over F2 – in fact they

100 CHAPTER 3. MODULES
uniquely exhaust the possibilities. Therefore we ﬁx a minimal polynomial and
ﬁnd the associated invariant factors the end with this minimal polynomial and
then move on.
The coeﬃcients of the polynomials of degree less than or equal to 2 corre-
spond to all length 3 binary words – excluding 000 and 001:
a(x) = x, b (x) = x + 1, c (x) = x2,
d(x) = x2 + 1, e (x) = x2 +x, f (x) = x2 +x + 1.
Now their associated invariant factors with the added condition that the total
degree fo the product of the invariant factors equal 2 so that the companion
matrices ﬁt in 2 × 2 matrices.
x|x →
[
0 0
0 0
]
;
x + 1|x + 1 →
[1 0
0 1
]
;
x2 →
[0 0
1 0
]
;
x2 + 1 →
[0 1
1 0
]
;
x2 +x →
[0 0
1 1
]
;
x2 +x + 1 →
[
0 1
1 1
]
.
□
87 Simultaneous Diagonalization Let V be a ﬁnite dimensional vectorHint: Consider the
eigenspaces of ϕ and ψ. space and let ϕ andψ be commuting diagonalizable linear transformations from
V to V . Show that ϕ and ψ can be simultaneously diagonalized.
Proof: If a ﬁnite dimensional linear transformation is diagonalizable over its
ﬁeld then it has all its eigenvalues in the ﬁeld (under some basis the matrix is
diagonal and the eigenvalues are simply those elements on the diagonal.)
If all the eigenvalues of a linear transform are the same then the associ-
ated diagonal matrix is scalar. If both ϕ and ψ are scalar then they are both
simultaneously diagonalized.
Now presume that without loss of generality that ϕ is not a scalar transform.
Hence there are at least two distinct eigenspaces. It follows each eigenspace of
ϕ has dimension less than that of V . Since ϕ(Ei) = Ei for any eigenspace Ei we
see that in fact that since ϕ andψ commute they leave each others eigenspaces
invariant – consider restricting to some eigenspace Ei of ϕ.
Now we setup an induction. When the dimension of V is 1, all linearly
transformations are scalar (Schur’s lemma). Suppose that for all vector spaces
of dimension n, any commuting diagonalizable linear transformations can be
simultaneously diagonalized. Then in the case where dim V =n + 1, either all
the two linear transformations are scalar and so simultaneously diagonalized,
or one is not scalar in which case its eigenspaces are proper subspaces. So we
restrict the maps to any eigenspace and by induction simultaneously diagonalize
on the this subspace. That the maps commutate means that they respect each
others eigenspaces and as such we can do this for all eigenspaces of V under the
non-scalar map until in the end we have both maps simultaneously diagonalized.

Algebra – James Wilson 101
□
88 Simultaneous Diagonalization Let V be a ﬁnite dimensional vector Hint: Consider the
eigenspaces of ϕi.space and let {ϕ}i∈I be a family of commuting diagonalizable linear transfor-
mations from V to V . Show that ϕi can be simultaneously diagonalized.
Proof: If a ﬁnite dimensional linear transformation is diagonalizable over its
ﬁeld then it has all its eigenvalues in the ﬁeld (under some basis the matrix is
diagonal and the eigenvalues are simply those elements on the diagonal.)
If all the eigenvalues of a linear transform are the same then the associated
diagonal matrix is scalar. If all ϕi are scalar then they are both simultaneously
diagonalized.
Now presume that without loss of generality that ϕi is not a scalar transform.
Hence there are at least two distinct eigenspaces. It follows each eigenspace of
ϕi has dimension less than that of V . Since ϕi(Ej) = Ej for any eigenspace Ej
we see that in fact that since all ϕi commute they leave each others eigenspaces
invariant – consider restricting to some eigenspace Ei of ϕi.
Now we setup an induction. When the dimension of V is 1, all linearly
transformations are scalar (Schur’s lemma). Suppose that for all vector spaces
of dimension n, any commuting diagonalizable linear transformations can be
simultaneously diagonalized. Then in the case where dim V =n + 1, either all
the two linear transformations are scalar and so simultaneously diagonalized,
or one is not scalar in which case its eigenspaces are proper subspaces. So we
restrict the maps to any eigenspace and by induction simultaneously diagonalize
on the this subspace. That the maps commutate means that they respect each
others eigenspaces and as such we can do this for all eigenspaces of V under the
non-scalar map until in the end we have both maps simultaneously diagonalized.
□
89 Matrices and Polynomials LetV be a 7-dimensional vector space over Hint: Construct the compan-
ion matrices of the invariant
factors to match dimension 7.
Q.
(a) How many similarity classes of linear transformations on V have character-
istic polynomial (x − 1)4(x − 2)3?
(b) Of the similarity classes in (a), how many have minimal polynomial ( x −
1)2(x − 2)3?
(c) Let ϕ be a linear transformation from V to V having characteristic poly-
nomial (x − 1)4(x − 2)3 and minimal polynomial ( x − 1)2(x − 2)3. Find
dim ker(ϕ − 2id).
Example:
(a) Leta = (x − 1) and b = (x − 2). Having ﬁxed the characteristic polynomial
we look at the possible invariant factors that give this polynomial. We now
the ﬁnal invariant factor is the minimal polynomial so it must have all the
roots of the characteristic. Thus both a and b divide the ﬁnal term.
Let a1,...,a k denote the powers of a in the order of the invariant factors,
and likewise b1,...,b l the powers for b. The algorithm to traverse each
invariant factor chain is given by the relations,
1 ≤a1 ≤ · · · ≤ ak ≤ 4, 1 ≤b1 ≤ · · · ≤ bl ≤ 3,
a1 + · · · +ak = 4, and b1 + · · · +bl = 3.

102 CHAPTER 3. MODULES
Notice the last two always force
a1 + · · · +ak +b1 + · · · +bl = 7
so that we need not explicitly make use of the fact that we have 7-dimensional
space.
This gives the following possible chains for ai’s:
A = 1, 1, 1, 1 1, 1, 2 1, 3 1, 4
2, 2
Forbj’s we get
B = 1, 1, 1 1, 2 3
Thus the total number of conﬁgurations is the product of the conﬁgurations
possible fora andb. This gives a total of 15. For clarity they are enumerated
below
A1,1 +B1 : a | ab | ab | ab
A1,1 +B2 : a | a | ab | ab2
A1,1 +B3 : a | a | a | ab3
A1,2 +B1 : ab | ab | a2b
A1,2 +B2 : a | ab | a2b2
A1,2 +B3 : a | a | a2b3
A2,2 +B1 : b | a2b | a2b
A2,2 +B2 : a2b | a2b2
A2,2 +B3 : a2 | a2b3
A1,3 +B1 : b | ab | a3b
A1,3 +B2 : ab | a3b2
A1,3 +B3 : a | a3b3
A1,4 +B1 : b | b | a4b
A1,4 +B2 : b | a4b2
A1,4 +B3 : a4b3
(b) Now assume instead that the invariant factor all conclude with a2b3. Ig-
noring the possible characteristic polynomials what are our options. We
redesign our algorithm slightly. The information that is missing now is
what the total multiplicity of powers is. We do however now the dimension
of our space to be 7 so we can add this to our deﬁning relations as follows:
1 ≤a1 ≤ · · · ≤ ak = 2, 1 ≤b1 ≤ · · · ≤ bl = 3,
a1 + · · · +ak +b1 + · · · +bl = 7.
If, for instance, we look at the ai’s separately we notice the length k is not
restricted. Thus we must make sure of the ﬁnal relation each time. Indeed
we see the subrelation
a1 + · · · +ak−1 +b1 + · · · +bl−1 = 2.
This means 1 ≤k − 1 +l − 1 ≤ 2 or simply 3 ≤k +l ≤ 4. Our options are
k = 1, l = 2, 3; l = 1, k = 2, 3; or k =l = 2. Thus we get the possibilities
b2|a2b3, b |b|a2b3, a 2|a2b3, a |a|a2b3, ab |a2b3.
There are 5 similarity classes with minimal polynomial a2b3.

Algebra – James Wilson 103
(c) Now we combine our results and notice that when a4b3 is the characteristic
polynomial and a2b3 the minimal polynomial, then the only choices for
invariant factors are
a|a|a2b3, a 2|a2b3.
To calculate the dimension of the null-space of the eigenspace associated
with the eigenvalue 2, we simply see the multiplicity of 2 is 3, so its eigen
space has dimension 3, and so the nullity is of dimension 3.
□
90 Minimal Polynomials Exhibit a 4 × 4 matrix A with integer coeﬃcients Hint: Notice the minimal
polynomial for any such A di-
vides x5 − 1.
such that A5 =I4 ⁄=A.
Example: As the relation A5 =I4 demonstrates, the minimal polynomial for
A divides x5 − 1. As A ⁄=I4 it follows the factor x − 1 is not the contributing
factor. So consider
p(x) = (x5 − 1) ÷ (x − 1) = x4 +x3 +x2 +x + 1.
Certainlyp(A) = 0 still as expressed above, and also as we want a 4 × 4 matrix
we may as well simply choose the companion matrix of p(x). So take
A =


0 0 0 −1
1 0 0 −1
0 1 0 −1
0 0 1 −1

.
As designed A5 =I4 and A ⁄=I4. □
91 Matrix Relations Let A,B ∈M5(Q) be non-zero 5 × 5 matrices over Q Hint: Compute the possible
invariant factors of A and B.such that AB =BA = 0. Prove that if A4 =A and B4 =B2 −B then A +B
is invertible.
Proof: From the relation A4 = A we know the minimal polynomial of A
dividesx4 −x, and as A ⁄= 0, it cannot be the factor x alone. Nor can it be the
factor x − 1 as A is a zero-divisor and as such not the identity. The rational
roots theorem tells us x2 +x + 1 is irreducible so there are no smaller factors.
However if the minimal polynomial is x2 +x + 1 then the invariant factors must
have a total degree which is even. As we have 5 × 5 matrix this cannot exist.
Also if no eigen value is 0, then the product of eigenvalues is a unit in Q so A
is invertible. However, invertible matrices are not zero-divisors. Hence we can
conclude that the only possibilities for minimal polynomials are:
x(x − 1), x (x2 +x + 1), x (x − 1)(x2 +x + 1).
Moving to B we notice the minimal polynomial divides x4 −x2 +x, and
again as B ⁄= 0 it is not only the factor x that accounts for the annihilation.
So the minimal polynomial must divide contain factors from x3 −x + 1. By
the rational roots theorem we see x3 −x + 1 is irreducible over Q; hence, the
minimal polynomial of B is precisely x4 −x2 +x. This means the stray eigen
value is 0 as the other roots are outside of Q. So the invariant factors of B are
x|x4 −x2 +x.
Now we invoke the property that AB = BA = 0. As the transformations
commute they respect each others eigenspaces. PENDING: ﬁnish □
92 Linear Decomposition LetV be a ﬁnite dimensional vector space over Hint: Consider a decomposi-
tion into eigenspace ﬁrst, and
then a decomposition into in-
variant factors.

104 CHAPTER 3. MODULES
a ﬁeld F . Let θ be a linear transformation on V . Assume that there do not exist
proper θ-invariant subspaces V1,V2 ofV such that V =V1 ⊕V2. Show that for
some basis of V the matrix of θ is the companion matrix of p(x)e, where p(x)
is some irreducible polynomial in F [x].
Proof: The minimal polynomial of θ is a product of irreducibles in F [x]. If
there are two are more irreducibles in the minimal polynomial, then the roots of
each determine distinct eigenspaces. As eigenspaces are respected by the map
from which they are determined, it follows this non-trivial decomposition is of
the type forbidden by the hypothesis. So we are forced to accept that there is
indeed only one irreducible component in the minimal polynomial.
Finally if there are more than one invariant factors, then we know
V =I1 ⊕ · · · ⊕In
where each Ii is generated by the invariant factor i. This decomposition is also
clearly respected by θ as it describes θ. Therefore there can only be on invari-
ant factor and this invariant factor must be the minimal polynomial which we
recently decided was simply a power of an irreducible in F [x]. □
93 Jordan Normal Form LetV be a ﬁnite dimensional vector space over Q.Hint:
Letθ be a linear transformation on V having characteristic polynomial (x − 2)4.
(a) Describe the possible Jordan normal forms for θ, and for each of these give
the minimal polynomial of θ.
(b) For each of the possibilities in (a) give the dimension of the 2-eigenspace of
θ.
(c) Assume that θ leaves invariant only ﬁnitely many subspaces of V . What
can be said about the Jordan normal form of θ?
Example: PENDING: ﬁnd the energy to do this one. □
94 Jacobson Module Let R be an artinian ring. Show that J(R) is aHint: Use the fact that
J(R) annihilates all simple R-
modules.
semi-simple left R-module if and only if J(R)2 = 0.
Proof: Let V =J(R) be a semi-simple left R-module. Suppose that
V =V1 ⊕ · · · ⊕Vn
is the decomposition into simple R-modules. From Nakayama’s Lemma we know
if J(R)Vi =Vi then Vi = 0. Since each Vi is simple as an R-module, it follows
J(R)Vi = 0 for each i. This means that J(R)V = 0. But now recall that
V =J(R) and we see that indeed J(R)2 = 0.
Now suppose that J(R)2 = 0. It is clear that J(R) is contained in the
annihilator of V =J(R), and as J(R)2 = 0 it is in fact the annihilator. There-
fore J(R) is a faithful R/J (R)-module. However, R is artinian, so R/J (R) is
semi-simple artinian. Thus every left R/J (R)-module is semi-simple. Now we
observe that we can use this decomposition into simple R/J (R)-modules back
toR-modules since J(R) annihilates all simple R-modules. Hence, V is a semi-
simple R-module, that is, J(R) is a semi-simple R-module. □
95 Simple Algebras Suppose that R is a ﬁnite dimensional simple F -Hint: NoteR is a matrix ring
over a division ring. algebra, for a ﬁeld F . Show that dimF R =n2e, where ne =dimF V for some
irreducible R-module V .

Algebra – James Wilson 105
Proof: Since are R is a ﬁnite dimensional simple F -algebra it follows it is
semi-simple artinian so indeed
R ∼=Mn(D).
Furthermore, D is an F -algebra and ﬁnite dimensional as well. However, as
soon as we ﬁll one component in a matrix, then to generate the full left ideal
we need to include the entire column. Thus we get a natural copy of V = Dn
as an irreducible R-module – irreducible because it is a minimal left ideal of R.
Finally letting e =dimF D we see:
dimF R =n2e, dim F V =ne.
□
96 Endomorphisms and Semi-simplicity Let F be a ﬁeld and V be a Hint:
ﬁnite dimensional F -vector space. Let θ ∈EndF (V ) have minimal polynomial
f (x) ∈F [x]. Let R be the subalgebra F [θ] of EndF (V ). Prove that R is semi-
simple artinian if and only if each prime factor of f (x) in F [x] has multiplicity
1.
Proof: Suppose R is semi-simple artinian.
By the theorem of Wedderburn-Artin we decompose R as
R =F [θ] = Mn1(D1) ⊕ · · · ⊕Mnk (Dk).
Since V is an F [x]-modules it also passes as an R-module. Moreover, it then
follows that V is an Mni(Di)-module.
In a PID primes correspond to irreducibles so we simply wish to prove that
f (x) is a product p1(x) · · ·pn(x) with each pi(x) irreducible and pi(x) = pj(x)
implying i =j.
PENDING: ﬁgure it out. □
97 Indecomposable Modules – True or False? For a short exact sequence Hint: Consider a cyclic group
with zero-divisors.
0 /d47/d47V /d47/d47W /d47/d47X /d47/d47 0
if V and W are indecomposable then so is X.
Example: False. Consider the following sequence of Z-modules:
0 /d47/d47 Z
6 /d47/d47 Z /d47/d47 Z6 /d47/d47 0.
As Z has no zero-divisors it can have no idempotents and so it is indecompos-
able. Yet clearly as Z-modules Z6 ∼= Z2 ⊕ Z3. □
98 Maximal Ideals Show that if M1,M 2,...,M n are distinct maximal ideals Hint: Use the third isomor-
phism theorem.of the commutative ring R, then each R-moduleR/Mi, 1 ≤i ≤n, is isomorphic
to exactly one factor of the chain
R ≥M1 ≥M1 ∩M2 ≥ · · · ≥ M1 ∩M2 ∩ · · · ∩Mn.
Proof: With the correct picture the result is an obvious interpretation of the

106 CHAPTER 3. MODULES
third isomorphism theorem.
R
/d111 /d111 /d111 /d111 /d111 /d111 /d111
a b
/d79/d79/d79/d79/d79/d79/d79
M1 a/d63/d63/d63 M2
/d127 /d127 /d127 b/d63/d63/d63 M3
/d127 /d127 /d127 c
M1 ∩M2b/d63/d63/d63 M2 ∩M3
/d127 /d127 /d127 c
M1 ∩M2 ∩M3c
We simply recurse.
R/Mi ∼=Mi−1/Mi−1 ∩Mi ∼=Mi−2 ∩Mi−1/Mi−2 ∩Mi−1 ∩Mi ∼= · · ·
∼=M1 ∩ · · ·Mi−1/M1 ∩ · · · ∩Mi.
As eachMi is distinct, so is each R/Mi and so each factor of the chain is uniquely
one of the R/Mi’s. □
99 Polynomial Rings – True or False? If R is a commutative artinianHint:
ring then R[x] is noetherian.
Proof: True.9
□
100 Injective Modules – True or False? Q is an injective Z-module.Hint: Show it is divisible.
Proof: Since Z is a PID it is suﬃcient to show Q is divisible. This means for
every n ∈ Z, nQ = Q. Certainly for every fraction a/b ∈ Q the fraction a/nb
is also in Q and thus n(a/nb) = a/b proving nQ = Q. So Q is an injective
Z-modules as it is divisible. □
101 Non-projective Modules Give three diﬀerent deﬁnitions of projectiveHint: For (ii) implies (iii) use
P = W , for (iii) implies (iv)
use the retract of the split se-
quence, for (iv) implies (ii) use
the pull-back of the diagram.
modules and show that your deﬁnitions are equivalent.
Theorem 3.0.11 All the following are equivalent in the category of left R-
modules:
(i) P is a projective R-module.
(ii) Given any map ϕ :P →W and another surjective map f :V →W , then
there exists a map ψ :P →V such that the following diagram commutes:
P
φ
/d15/d15ψ/d126/d126/d125 /d125 /d125 /d125
V f
/d47/d47W /d47/d47 0.
(iii) Every short exact sequence:
0 /d47/d47U /d47/d47V
f /d47/d47P /d47/d47 0
splits.
9By the Hilbert basis theorem, R[x] is noetherian because R is commutative and noetherian.

Algebra – James Wilson 107
(iv) If P is a quotient module of V then it is also a direct summand of V ; so
there exists an embedding P ′ ∼= P in V and a complement U such that
V =P ′ ⊕U .
Proof: (i) implies (ii) and (ii) implies (i) by the very deﬁnition of projective
modules.
Now consider why (ii) implies (iii). If we take a short exact sequence
0 /d47/d47U /d47/d47V
f /d47/d47P /d47/d47 0
and let W in (ii) be equal to P , together with ϕ = idP , then we immediately
have the picture:
P/d79/d79
idP
/d15/d15ψ/d127/d127/d126 /d126 /d126 /d126 /d126 /d126 /d126
0 /d47/d47U /d47/d47V
f /d47/d47P /d47/d47 0.
As (ii) tells us, ψf = idP . However this is an equivalent condition for a short
exact sequence to be split exact – we now have a retract ψ. Therefore (ii) implies
(iii).
Assume (iii) now and let P be a quotient of a module V . It follows we
we have surjection f : V → P with kernel U . Thus we have the short exact
sequence:
0 /d47/d47U /d47/d47V
f /d47/d47P /d47/d47 0.
From our assumption of (iii) we know this short exact sequence splits so indeed
P can be embedded in V as a direct summand – (iv).
Finally assume (iv) is true, and assume we have a surjection
f : V → W and a map ϕ : P → W . Then consider the pull-back of the
diagram:
P
φ
/d15/d15
V f
/d47/d47W /d47/d47 0,
X
πP /d47/d47
πV
/d15/d15
P
φ
/d15/d15
V f
/d47/d47W /d47/d47 0
where X = {(v,p ) ∈ V ⊕P : f (v) = φ(p)} and where πP (v,p ) = p and
πV (v,p ) = v. Given any p ∈ P , φ(p) ∈ W so there exists a v ∈ V such that
f (v) = φ(p). Hence ( v,p ) ∈ X and πP (v,p ) = p proving that πP is surjective.
Therefore P splits in X by the assumption of (iv). Use the map i :P →X as
the retract for πP . Then we see the composition πVi :P →V and furthermore,
fπVi(p) = f (πV (v,p )) = f (v) = φ(p)
by design. So the diagram commutes:
P
φ
/d15/d15
πVi
/d126/d126/d125 /d125 /d125 /d125 /d125 /d125 /d125 /d125
V f
/d47/d47W /d47/d47 0.
Therefore P is projective. □
102 Projective Z-modules Prove Q is not a projective Z-module by Hint: Suppose Z < Q < F
the consider F/Z> Q/Z and
the torsion of each quotient
module.

108 CHAPTER 3. MODULES
showing it is not a direct summand of a free Z-module.
Proof: 10 SupposeF is any free Z-module containing Q. As it stands, F ∼= ⊕iZ.
Since Q is embedded in F , we may take the principle copy of Z inside Q and
create a tower of Z ≤ Q ≤ F through which we quotient by Z to obtain:
F/Z ≥ Q/Z.
Q/Z corresponds to the rational points on the unit circle so we visibly have
an inﬁnite amount of torsion; more speciﬁcally, we have torsion of every posi-
tive order. However, given any Z embedded in F , there corresponds a generator
v ∈ F , such that Z = Zv in F . Yet F is a direct sum, so v must be almost
everywhere 0. This means no matter how large F is, we can only factor out,
non-trivially, a ﬁnite number of components. So while factors exist that cre-
ate torsion, there is insuﬃcient to create the inﬁnite amount that is created
by quotienting Q by Z. Thus Q/Z cannot be a submodule of F/Z so by the
correspondence theorem, Q is not embedded in F and hence cannot be a direct
summand either. □
103 Non-projective Modules Show a ﬁeld of characteristic 0 is not aHint: Show that they contain
Q and that Q is not contained
in a free module (Exercise-
3.102.)
projective Z-module under the regular action.
Proof: Every ﬁeld of characteristic 0 contains a subﬁeld isomorphic to Q.
However, from Exercise- 3.102, Q is not a direct summand of a free Z-module.
Moreover, the proof indicates that Q is indeed not even a submodule of a free
Z-module. Hence, no ﬁeld of characteristic 0 is a submodule of a free Z-module
and hence it may not be a direct summand of a free Z-module. This charac-
terization describes all projective modules; thus, no ﬁeld of characteristic 0 is a
projective Z-module. □
104 Cyclic Projective Modules Let R be a PID. Which cyclic R-modulesHint: Only 0 and R work.
are projective?
Example: LetV =Rv be a cyclic R-module. Without loss of generality assume
V ⁄= 0.
Deﬁne the map f :R →Rv byf (x) = xv. Since
f (rx +y) = (rx +y)v =r(xv) +yv =rf (x) +f (y)
and multiplication is well-deﬁned, we have a nice R-linear map. Also, any
xv ∈Rv is clearly hit by x, so f is surjective. Finally if the kernel of f is trivial
then we attain an isomorphism of R-modules. Thus R ∼=Rv whenever xv = 0
implies x = 0.
So we may say, any cyclic R-module with trivial annihilator is projective,
simply because it is isomorphic to R as a regular left R-module, and R is free
as an R-module.
Now assume Ann(V ) ⁄= 0, so the kernel is non-trivial; then rv = 0 for some
non-zero r ∈R. Thus V contains torsion elements by deﬁnition. However, free
R-modules must be torsion free, so they cannot contain V as a submodule, let
alone as a direct summand. Hence such cyclic modules are not projective. □
105 Projective/Injective Inheritance Let R be commutative. Prove orHint: The category of Z4-
modules provides all the nec-
essary counter-examples.
Disprove:
(i) Every submodule of a projective R-module is projective.
10An equivalent way to show Q is not projective is to observe every projective module over
a PID is free. Yet Q is not free as any two rational numbers are linearly dependent over Z.

Algebra – James Wilson 109
(ii) Every submodule of and injective R-module is injective.
(iii) Every quotient of a projective R-module is projective.
(iv) Every quotient of a injective R-module is injective.
Example: Let R = Z/4. Consider the short exact sequence:
0 /d47/d47 Z/2 /d47/d47 Z/4 /d47/d47 Z/2 /d47/d47 0.
It does not split as Z/4 is not isomorphic to Z/2 ⊕ Z/2. However as it does not
split we see the Z/2 as Z/4-module is not projective because it is the left term
of a short exact sequence that does not split. Visibly, Z/2 is both a submodule
and a quotient modules of a projective module (the ring is always a free module
under the regular action, and thus projective), but it itself is not projective.
If we can show that Z/4 is injective over itself we will be able to conclude
that Z/2 is not an injective module as the sequence does not split, and it is the
left term of the sequence. Thus, neither as a submodule, nor as a quotient is it
injective. To show Z/4 is injective requires only that we show it is injective on
left ideals of Z/4, namely, 0, 2Z/4, and Z/4. Fix the picture:
Z/4
0 /d47/d47L
f
/d79/d79
i /d47/d47 Z/4
g
/d97/d97/d68 /d68 /d68 /d68
Since Hom Z/4(0, Z/4) = 0, when L = 0 we see f = 0 so we extend the map
with the trivial map: g(x) = 0.
Now suppose the left ideal is Z/2. Now Hom Z/4(Z/2, Z/4) has only two
maps: the trivial map and inclusion. If f is the trivial map then g is trivial and
properly extends f . When f is inclusion, we let g be the identity map.
Finally suppose the left ideal is Z/4 itself. Here we trivially let f =g. Since
these extensions work for all left ideals, it proves by Baer’s Criterion that Z/4
is injective over itself. □
106 Injective Z/nZ-modules Let n ≥ 1. Then Z/nZ is injective Z/nZ- Hint: Any cyclic module ho-
momorphism is determined by
where the generator is sent.
module.
Proof: We make use of Baer’s Criterion. The (left) ideals of Z/nZ aremZ/nZ.
Thus we need only consider extending our maps
Z/nZ
0 /d47/d47mZ/nZ
f
/d79/d79
i /d47/d47 Z/nZ
g
/d100/d100/d73 /d73 /d73 /d73 /d73
Since everything is cyclic, we notice f is determined by where m is mapped,
say f (m) = k. To be deﬁned, m must divide n and so n = am and thus
0 = f (am) = af (m) = ak, so indeed am|ak and m|k. Hence, k =lm for some
l, so f is multiplication by l. Deﬁne g : Z/nZ → Z/nZ byg(x) = lx. Certainly
this is Z/nZ-linear and also agrees with f on mZ/nZ. As any left ideal map
can be extended, Z/nZ is injective. □
107 Injective Z-modules – True or False? Every abelian group monomor- Hint: ShowZp∞ is divisible.
phism Zp∞ →A splits.

110 CHAPTER 3. MODULES
Proof: True. It suﬃces to show Zp∞ is injective, and for this we show it is
divisible as a Z-module. Take any m ∈ Z such that m ⁄= 0; then we need to
show for all a
pi + Z ∈ Zp∞ that there exists a b
pj + Z such that
a
pi ≡m b
pj (mod Z).
We begin with generators: Let m =kpl so that (k,p ) = 1. As such we know
there exists integers s and t such that: sk +tpi = 1, equivalently: pi|sk − 1, or
1
pi ≡ sk
pi ≡m s
pi+l (mod Z).
Thus each generator is divisible, but this is temporary for certainly then:
a
pi ≡m as
pi+l (mod Z),
and so in fact Zp∞ is divisible. □
108 Projectives over PIDs – True or False? Q[x,x −1] is a projectiveHint: Show Q[x,x −1] is not
free. Q[x]-module.
Proof: Q[x,x −1] will be projective only if it is a free Q[x]-module, since Q[x] is a
PID. Clearly any basis must be of size 2 or greater. If we select any two elements
from Q[x,x −1], q =∑l
i=−kqixi and p =∑n
i=−mpixi then xkq,xmp ∈ Q[x] so
we have a =xmpxk and b =xkqxm both in Q[x] and also
((xmp)xk)q − ((xkq)xm)p =xmpxkq −xmpxkq = 0.
Therefore any two elements of Q[x,x −1] are Q[x]-linearly dependent so that
Q[x,x −1] has no basis and is not free. □
109 Module Quotients LetR be a ring and V ≤W ,V ′ ≤W ′ beR-modulesHint: Notice that R is projec-
tive so it is a direct summand
of W and W ′.
such that W/V ∼=R ∼=W ′/V ′ and V ∼=V ′ then W ∼=W ′.
Proof: SinceR is projective it follows every short exact sequence that ends in
R splits. Thus
0 /d47/d47V /d47/d47W /d47/d47R /d47/d47 0
and
0 /d47/d47V ′ /d47/d47W ′ /d47/d47R /d47/d47 0
split, so indeed W =V ⊕R and W ′ ∼=V ′ ⊕R. But V ∼=V ′ so W ∼=W ′.11 □
110 Injectivity of Fraction Fields Let R be an integral domain and F itsHint: Use Baer’s Criterion.
ﬁeld of fractions. Prove that F is an injective R-module.
Proof: We make use of Baer’s Criterion. So consider the following diagram,
I ⊴R:
RF
0 /d47/d47 RI
f
/d79/d79
i /d47/d47 RR
g
/d97/d97/d67 /d67 /d67 /d67
11A truly convincing proof here uses the 5-lemma on the short exact sequence with the
middle map deﬁned by the split map from W to V , followed by the isomorphism of V to V ′
followed by the inclusion of V ′ to W ′.

Algebra – James Wilson 111
Given non-zero values a,b ∈I it is clear by linearity that
af (b) = f (ab) = f (ba) = bf (a); f (a)/a =f (b)/b =c.
Deﬁneg(r) = rc and clearly for any non-zero a ∈I it follows g(a) = af (a)/a =
f (a), so g extends f .12 Moreover, g(sx +y) = sxc +yc = sg(x) + g(y) so
it is R-linear. Hence g extends f so by Baer’s Criterion F is injective as and
R-module. □
111 Injective Hulls – True or False? Q is the injective hull of Z. Hint:
Deﬁnition 3.0.12 Given R-modulesX ≤Q, and Q′, with Q and Q′ injective
R-modules, then Q is an injective hull (injective envelope) of X if given any
monomorphism g : X → Q′ there exists a monomorphism h : Q → Q′ so that
the following diagram commutes:
0
/d15/d15
0 /d47/d47X
g
/d15/d15
i /d47/d47Q
h
/d127/d127/d127 /d127 /d127 /d127
Q′
Proof: True. We see Q is divisible as nQ = Q for any n ∈ Z, n ⁄= 0. Clearly
Z ≤ Q. Now take any other injective module Q′ with Z embedded via a map
g : Z →Q′. As Q′ is injective over Z it is divisible by Z. So nQ′ =Q′ for any
n.
Take 1 ∈Q′ to be the element g(1). Then for all b ∈ Z, b ⁄= 0, bQ′ =Q′ so
there exists an element c ∈Q′ such that bc = 1. Now suppose c′ ∈Q′ also has
the property that bc′ = 1. Then bc = bc′ and so b(c −c′) = 0. Let x = c −c′.
If x = 0 we are done. If x ⁄= 0 then bx = 0 tells us there must be a y ∈ Q′
such that bx1 = x. But then b2x1 = 0 and we repeat. In the end bn+1xn = 0
for all n so in the end x∞ has no y ∈ Q such that by ⁄= x∞ as then b2y = 0.
in Q′ then Thus given any a/b ∈ Q, there exists a c ∈Q′ such that bc =g(a).
Deﬁne h : Q → Q′ as h(a/b) = c. Suppose that c′ ∈ Q′ also has the property
that bc′ =g(a). Then
As (b, 1) = 1, there are integers n,m such that 1 = mb +n1 □
112 Semi-simple Modules Every short exact sequence of C[x]/(x2 − 1)- Hint: Show that the ring is
semi-simple artinian.modules splits.
Proof: It is suﬃcient to show that C[x]/(x2 − 1) is semi-simple artinian; for
then every module is injective and projective, and so every short exact sequence
splits. Let I = (x2 − 1). Notice that the only proper ideals are (( x − 1) +I)
and ((x + 1) +I). This intersect trivially, and their sum is the entire ring, thus
C[x]/(x2 − 1) has a complement for every submodule over itself, so it is semi-
simple artinian. □
113 Semi-simple Modules – True or False? Every short exact sequence Hint: Show that Z15 is semi-
simple artinian.over Z15-modules splits.
Proof: True. Notice Z15 ∼= Z3 ⊕ Z5 which is the form of the Wedderburn-Artin
theorem, so Z15 is semi-simple artinian. Hence, every module is projective and
12 Assume that R is canonically embedded in F already so that rc is well-deﬁned.

112 CHAPTER 3. MODULES
injective, so every short exact sequence splits. □
114 Projective R[x]-modules – True or False? Every R[x]-module isHint: Show R[x] is not ar-
tinian. projective.
Example: False. If every module is projective, then every short exact sequence
splits, and consequently every module is also injective. This shows every sub-
module has a complement, so every module is semi-simple. But this is a condi-
tion equivalent to requiring that R[x] be semi-simple artinian. Thus if R[x] is
not, then some submodule is not projective. Clearly the chain
(1) ≥ (x) ≥ (x2) ≥ · · ·
is an inﬁnite descending, never stabilizing, chain, so R[x] is not artinian. □
115 Projectivity and Freeness – True or False? Every projective moduleHint: Consider any ring prod-
uct ring. over a commutative ring is free.
Example: False. Let the ring be R = Z/2 ⊕ Z/2. If we deﬁne Z/2 as a
left Z/2 ⊕ Z/2-module by noticing I = ((1, 0)) is a left ideal of R. Moreover,
J = ((0, 1)) is also a left-ideal and I ⊕J = R so I is a direct summand of R.
YetI has order 2, not a multiple of 4, so it cannot be a free R-module, yet it is
still projective. □
116 Dual Modules Let F be a free left R-module with ﬁnite basis. ProveHint: Map a basis {ei} to
{εi} where εi(ej) = δij – the
Kronecker delta.
that F ∗ is a free right R-module with ﬁnite basis dual to the basis of F . Prove
that F is reﬂexive.
Proof: Lete1,...,e n be a basis for F . Deﬁne the linearly functionals εi(ej) =
δij and extend ϵi by linearization. Deﬁne the map E from RF to F ∗
R =
HomR(RF,RRR) as ei ↦→ϵi and generalize by linearization as follows:
n∑
i=1
λiei ↦→
n∑
i=1
εili.
The map is clearly well-deﬁned and R-linearly. Now take any f ∈F ∗. It follows
f (x) = f
( n∑
i=1
λiei
)
=
n∑
i=1
λif (ei) =
n∑
i=1
λifiεi(ei) =
n∑
i=1
fi
n∑
i=1
εi(λiei) =
n∑
i=1
fiεi(x).
Therefore f =f1ε1 + · · · +fnεn and so ε1,...,ε n is a basis of F ∗
R. So not only
is F ∗
R ﬁnite dimensional, it has the same dimension as F ; thus by the universal
property of free modules, F ∼=F ∗ as they are free on cardinally equivalent bases.
Hence F ∼=F ∗∗ provingF is reﬂexive. □
117 Duals of Projectives LetP be a ﬁnitely generated projective R-module.Hint: Use the fact that P is
a direct summand of a free
module and the already proven
result for free modules – see
Exercise-3.116.
Prove that P ∗ is a ﬁnitely generated projective right R-module, and that P is
reﬂexive. Demonstrate that both statements may be false if P is not ﬁnitely
generated.
Proof: Let {v1,...,v n} be a set of generators for P . We may deﬁne the
Kroneckerδi,j maps as δi,j = 0 when i ⁄=j and 1 when i =j. From this we may
deﬁne the maps fi : P → R by fi(vj) = δi,j, and generalized linearly. These
maps lie in P ∗ = HomR(RP,RRR), which is a right R-module. Furthermore,
as P is generated by {v1,...,v n} we may take any map g ∈ P ∗ and express

Algebra – James Wilson 113
g = gf1 + · · ·gfn. Thus P ∗ is ﬁnitely generated. Moreover, we may show
P ∗∗ ∼=P with the following isomorphism:
ϕ :p ↦→ (ϕp :g ↦→g(p)).
Supposeϕp =ϕq. Then for all g ∈P ∗ it follows g(p) = g(q). However, we know
fi(vi) = 1 while fi(vj) = 0 for all i ⁄=j so letting g =fi we see the requirement
that p =q; thus the map is injective.
That ϕ is linear follows from the linearity in each component:
ϕsp+q(g) = g(sp +q) = sg(p) +g(q) = sϕp(g) +ϕq(g).
All that remains is surjectivity. Recall that P ∗ is generated by {f1,...,f n}.
Now take any ψ ∈P ∗∗. Clearly
ψ(r1v1 + · · · +rnvn) = r1ψ(v1) + · · · +rnψ(vn).
Now provided ψ(v1),...,ψ (vn) generate P ∗∗ we are done. But certainly this
is true because each ψ(vi)(fj) = δi,j = gi(fj), where {gi} is a basis for P ∗∗.
(Notice the size of the generating sets in P , P ∗, and P ∗∗ are all equal.)
To showP ∗ is projective consider the characterization of projective modules
as a direct summand of a free module. Recall that
HomR
( n⨁
i=1
RRR,RRR
)
=
n∏
i=1
HomR(RRR,RRR) =
n∏
i=1
RRR =
n⨁
i=1
RRR.
Moreover,P is ﬁnitely generated so it is a direct summand of a ﬁnitely generated
free R-module (consult the proof of the characterization to verify ﬁniteness is
implied.) Finally, HomR(−,RRR) takes split exact sequences to split exact
sequences, so we obtain:
0 /d47/d47P /d47/d47
Hom(−,R)
/d15/d15
⨁n
i=1RRR
Hom(−,R)
/d15/d15
/d47/d47Q
Hom(−,R)
/d15/d15
/d47/d47 0
0 /d47/d47P ∗ /d47/d47⨁n
i=1RRR /d47/d47Q∗ /d47/d47 0
Since we now see P ∗ is a direct summand of a free R-module it is clear that P ∗
is projective. □
Example: If we let P =⨁
N F2 then it is projective as it is a module in the
category of semi-simple artinian ring. However P ∗∗ has cardinality 2 ℵ0 > ℵ0 so
P is not isomorphic to P ∗∗. So P is not reﬂexive.
Now suppose P = ⨁
N Z. As coproducts of projectives are projective we
knowP is projective. However, once again, P ∗ is∏
N Z which is not projective
as it is not a direct summand of a free module. □
118 Finite Dimensional Duals LetV be a ﬁnite dimensional vector space Hint: Use Exercise- 3.116.
over a division ring D. Prove that V is reﬂexive.
Proof: SinceV is a vector space it is a free module. Thus V ∗ is a free module
of the same rank (Exercise- 3.116) and so V ∼=V ∗∗. □
119 Projectivity and Fields Prove that a domain R is a ﬁeld if and only if Hint: Use the Wedderburn-
Artin theorem to characterize
R.
everyR-module is projective.
Proof: Let R be an integral domain.

114 CHAPTER 3. MODULES
Suppose that every R-module is projective. Then every short exact sequence
splits so every module is semi-simple. Thus R is semi-simple artinian. Applying
Wedderburn-Artin we see
R ∼=Mn1(D1) ⊕ · · ·Mnk (Dk).
Yet k = 1 or otherwise the decomposition reveals zero-divisors, for instance
In1 ⊕ 0 · · · ⊕ 0 and 0 ⊕ · · · ⊕ 0 ⊕Ink . Also R is commutative so n1 = 1 and D1
is commutative. Therefore R is the ﬁeld D1.
Now suppose that R is a ﬁeld. Then R is semi-simple artinian so every short
exact sequence splits. In particular every module is projective. □
120 Subring Tensors Let R be a subring of the ring S such that S is aHint: Use the middle linear
property of tensors. free right R-module with basis {si : i ∈I}. If V is a left R-module, then, as
abelian groups,
S ⊗RV =
⨁
i∈I
si ⊗V,
where si ⊗V denotes the subspace of S ⊗RV generated by all pure tensors of
the form si ⊗v.
Proof: Recall the submodule generated by each si is siR. So indeed we have:
S ⊗RV =
(⨁
i∈I
siR
)
⊗V =
⨁
i∈I
siR ⊗V =
⨁
si ⊗V,
where we observe that any element sir ⊗v can be written as si ⊗rv and thus
ﬁts our given form. □
121 Tensors over PIDs Let V and W be Z-modules.Hint: Use the universal prop-
erty of tensors to construct the
maps. Do not forget to invert
each for the isomorphism.
(i) V ⊗ Z/mZ ∼=V/mV .
(ii) Z/mZ ⊗ Z/nZ ∼= Z/kZ where k = (m,n ).
(iii) Describe V ⊗W if V and W are ﬁnitely generated.
Proof:
(i) Deﬁne the map f :V × Z/mZ →V/mV by (v,k) = kv. Given any k ≡j
(mod m) if follows k −j =l ·m so that indeed
(kv +mV ) − (jv +mV ) = (k −j)v +mV =l ·mv +mV =mV ;
therefore, kv ≡jv (mod mV ), and f is well-deﬁned. Also
f (rv,k) = krv =rkv =f (v,rk)
for all r ∈ Z. Finally:
f (v +w,k) = kv +kw =f (v,k) +f (w,k)
and
f (v,k +j) = kv +jv =f (v,k) +f (v,j);
hence, f is Z-balanced and so by the universal property of tensors there
exists a Z-balanced map (furthermore a group homomorphism as Z is
commutative so the tensor product is again a Z-module and the induced
maps Z-homomorphisms): ˜f :V ⊗ Z/mZ →V/mV which covers f .

Algebra – James Wilson 115
Now deﬁne its inverse as: g :V/mV →V ⊗ Z/mZ byg(v +mV ) = v ⊗ 1.
Clearly
˜f (g(v +mV )) = ˜f (v ⊗ 1) = f (v, 1) = 1v +mV =v +mV.
Also
g( ˜f (v ⊗k)) = g(f (v,k)) = g(kv +mV ) = kv ⊗ 1 = v ⊗k.
Thusg andf are indeed inverses and so f is a bijective Z-homomorphism
and thus a module isomorphism.
(ii) Let V = Z/mZ. From part (i) we see that V ⊗ Z/nZ = V/nV so in our
situation we have Z/mZ ⊗ Z/nZ = ( Z/nZ)/m(Z/nZ). However, this is
nothing more than Z/(m,n )Z.
(iii) If V and W are ﬁnitely generated we may decompose them as:
V ∼= Z/d1Z ⊕ · · · ⊕ Z/dkZ; W ∼= Z/e1Z ⊕ · · · ⊕ Z/elZ,
where d1|d2| · · · |dk, and e1| · · · |el and we allow di and ei to be 0 if free
parts appear. By distributing and using part (ii) we see:
V ⊗W ∼= (Z/d1Z ⊗W ) ⊕ · · · ⊕ (Z/dkZ ⊗W )
∼= (Z/d1Z ⊗ Z/e1Z) ⊕ · · · ⊕ (Z/d1Z ⊗ Z/elZ)
...
⊕(Z/dkZ ⊗ Z/e1Z) ⊕ · · · ⊕ (Z/dkZ ⊗ Z/elZ)
∼=
k,l⨁
i=1,j=1
Z/(di,ej)Z.
□
122 Torsion and Tensors – True or False? If V is a torsion module over Hint: Pull across the the pure
tensors, any annihilator of any
torsion elements.
R a PID and Q any ﬁeld containing R. Then V ⊗Q = 0.
Proof: True. Given any element a ∈V , let (p) be the order ideal of a. Since
V is a torsion module over a PID, we know p ⁄= 0. Thus p−1 exists in Q.
Furthermore we now see given any pure tensor q ⊗a we have:
q ⊗a = q
pp ⊗a = q
p ⊗pa = q
p ⊗ 0 = 0.
As every pure tensor is 0, the entire group is trivial. □
123 Fraction Field Tensors – True or False? Q ⊗ Q ∼= Q? Hint: Normalize one compo-
nent of each pure tensor.Proof: True. Deﬁne f : Q × Q → Q byf (q,p ) = qp. Since products in Q are
well-deﬁned, so is this map. Now take any r ∈ Z, certainly
f (qr,p ) = qrp =f (q,rp )
and s ∈ Q also yields:
f (s+q,p ) = sp+qp =f (s,p )+f (q,p ); f (q,s +p) = qs+qp =f (q,s )+f (q,p ).
Therefore, f is Z-balanced so it induces a Z-balanced (and furthermore, Z-
linear), map ˜f : Q ⊗ Q → Q. Now we must simply invert the map.

116 CHAPTER 3. MODULES
Takeg : Q → Q ⊗ Q by g(q) = q ⊗ 1. Clearly this map is well-deﬁned and
now we check it is an inverse:
˜f (g(q)) = ˜f (q ⊗ 1) = f (q, 1) = q · 1 = q.
g( ˜f (q ⊗p)) = g(f (q,p )) = g(qp) = qp ⊗ 1.
Now we must show that q ⊗p = qp ⊗ 1. To begin with notice m(p ⊗q) = 0
implies mp = 0 or mq = 0. But assuming p ⊗q ⁄= 0 then q ⁄= 0 and q ⁄= so
mp ⁄= 0 and mq ⁄= 0 unless m = 0 – we have a torsion free module. Now notice:
bd
(a
b
c
d ⊗ 1
)
=ac ⊗ 1 = a ⊗c
and
bd
(a
b ⊗ c
d
)
=a ⊗c;
therefore,
bd
(a
b
c
d ⊗ 1 − a
b ⊗ b
c
)
= 0.
Sense we have a torsion free module this means we have:
pq ⊗ 1 = a
b
c
d ⊗ 1 = a
b ⊗ c
d =p ⊗q.
Thus f and g are inverse maps, and f is a homomorphism, so f is an isomor-
phism. □
124 Tensor Isomorphisms – True or False? Let V be a right R-moduleHint: Both are false.
and W be a left R-module. True or False?
(i) There is an isomorphism of abelian groups V ⊗RW ∼=V ⊗ZW ?
(ii) If v ⊗w =v′ ⊗w′ in V ⊗RW , then v =v′ and w =w′.
Example: Both are false. For (i) consider letting R = Z ⊕ Z. Then
Z ⊕Z⊕Z Z ⊕ Z = Z; Z ⊕Z Z ⊕ Z = Z ⊕ Z.
For (ii) consider 2 ⊗ 3 = 1 ⊗ 6 in Z ⊗ Z. Certainly 2 ⁄= 1 and 3 ⁄= 6. □
125 Tensors and Quotients If V ′ is a submodule of the right R-moduleHint: Use the universal prop-
erty in both directions. V and W ′ is a submodule of the left R-module W , then (V/V ′) ⊗R (W/W ′) ∼=
(V ⊗RW )/U , where U is the subgroup of V ⊗RW generated by all elements of
the form v′ ⊗w and v ⊗w′ with v′ ∈V ′ and w ∈W , and v ∈V and w′ ∈W .
Proof: Declareg :V ×W →V/V ′ ⊗W/W ′ byg(v,w ) = (V ′ +v) ⊕ (w +W ′).
First our map is well-deﬁned as the cosets lie in the image not the domain. Next
we must verify this map is R-balanced:
g(vr,w ) = ( V ′ +vr) ⊗ (w +W ′) = (V ′ +v) ⊗ (rw +W ′) = g(v,rw );
g(v +u,w ) = V ′ + (v +u) ×w +W ′
= (( V ′ +v) ⊗ (w +W ′)) + ((V ′ +u) ⊗ (w +W ′))
= g(v,w ) +g(u,w );
g(v,w +u) = ( V ′ +v) × ((w +u) +W ′)
= (( V ′ +v) ⊗ (w +W ′)) + ((V ′ +u) ⊗ (u +W ′))
= g(v,w ) +g(v,u ).

Algebra – James Wilson 117
Asg isR-balanced it induces an R-balanced map g :V ⊗W →V/V ′ ⊗W/W ′.
Furthermore, on pure tensors alone g is surjective, thus we need only look for
its kernel to establish an isomorphism.
Notice indeed given any v′ ∈V ′ and any w ∈W that
g(v′ ⊗w) = g(v′,w ) = (V ′ +v′) ⊗ (w +W ′) = 0 ⊗ (w +W ′) = 0.
Likewise given w′ ∈ W ′ and v ∈ V we have g(v ⊗w′) = 0. Therefore U is
contained in the kernel of g. Thus we have g factors through U so we may
abusively write:
g :V ⊕W/U →V/V ′ ⊗W/W ′.
Now we look to construct an inverse map.
NoticeU =V ′ ⊗W +V ⊗W ′ and declare f :V/V ′ ×W/W ′ →V ⊗W/U by
f (V ′ +v,w +W ′) = v ⊗w +U.
First we must verify the f is well-deﬁned. Given V ′ +v =V ′ +u andw +W ′ =
x +W ′ we see v −u ∈V ′ and w −x ∈W ′ so:
f (V ′ + (v −u), (w −x) +V ′) = (v −u) ⊗ (w −x) +U =U ;
therefore, f is well-deﬁned. Moreover f is middle linear:
f (V ′ +vr,w +W ′) = vr ⊗w +U =v ⊗rw +U ;
f ((V ′ +v) + (V ′ +u),w +W ′) = f (V + (v +u),w +W ′) = (v +u) ⊗w +U
= ( v ⊗w +U ) + (u ⊗w) +U =f (V ′ +v,w +W ′) +f (V ′ +u,w +W ′);
f (V ′ +v, (w +W ′) + (x +W ′)) = f (V ′ +v, (w +x) +W ′) = v ⊗ (w +x) +U
= ( v ⊗w +U ) + (v ⊗x +U ) = f (V ′ +v,w +W ′) +f (V ′ +v,x +W ′).
Therefore we have an induced map on the tensor which visibly is the inverse of
g. Therefore we have an isomorphism of groups. □
126 Tensors of Exact Sequences If Hint: Use the split to dis-
tribute the tensor then con-
sider the components of the
sequence.
0 /d47/d47A
f /d47/d47C
g /d47/d47B /d47/d47 0
is split exact sequence of left R-modules, then
0 /d47/d47X ⊗RA
idX ⊗f/d47/d47X ⊗RC
idX ⊗g /d47/d47B /d47/d47 0
is an exact sequence of abelian groups for any right R-module X.
Proof: Since our given sequence splits it follows C ∼=A⊕B so we may consider
instead the following diagram:
A
ιA
/d15/d15
0
/d32/d32/d64/d64/d64/d64/d64/d64/d64
0 /d47/d47A
g /d47/d47
1A
/d63/d63/d126/d126/d126/d126/d126/d126/d126
0 /d31/d31/d64/d64/d64/d64/d64/d64/d64 C
f /d47/d47
πA
/d79/d79
πB
/d15/d15
B /d47/d47 0
B
ιB
/d79/d79
1B
/d62/d62/d126/d126/d126/d126/d126/d126/d126
Now we tensor with X and notice that
X ⊗C ∼=X ⊗ (A ⊕B) = (X ⊗A) ⊕ (X ⊗B).

118 CHAPTER 3. MODULES
Moreover, this sequence splits naturally. Thus we see componentwise the above
sequence with tensors is exact. Speciﬁcally we have the following natural con-
struction:
X ⊗A
1X ⊗ιA
/d15/d15
0
/d40/d40/d82/d82/d82/d82/d82/d82/d82/d82/d82/d82/d82/d82/d82
0 /d47/d47X ⊗A
1X ⊗g /d47/d47
1X ⊗1A
/d54/d54/d109/d109/d109/d109/d109/d109/d109/d109/d109/d109/d109/d109/d109
0 /d40/d40/d81/d81/d81/d81/d81/d81/d81/d81/d81/d81/d81/d81/d81 X ⊗C
1X ⊗f /d47/d47
1x⊗πA
/d79/d79
1X ⊗πB
/d15/d15
X ⊗B /d47/d47 0.
X ⊗B
1X ⊗ιB
/d79/d79
1X ⊗1B
/d54/d54/d109/d109/d109/d109/d109/d109/d109/d109/d109/d109/d109/d109/d109
□
127 Flat Modules Prove that a projective module is ﬂat.Hint: Use the fact that pro-
jectives are direct summands
of free modules and the visi-
ble fact that free modules are
ﬂat.
Proof: Given a projective module P there exists a module Q such that F =
P ⊕Q is a free R-module. A free module is isomorphic to ⨁R for some index
set so we observe given any module A that F ⊗A ∼=⨁A. Thus given a short
exact sequence:
0 /d47/d47A
f /d47/d47B
g /d47/d47C /d47/d47 0
it follows:
0 /d47/d47F ⊗A
1⊗f /d47/d47F ⊗B
1⊗g /d47/d47F ⊗C /d47/d47 0
is short exact as it is componentwise, and each element in the sequence is a
coproduct (universal property of coproducts infers the exactness on the entire
coproduct.) But now we translate the information using F =P ⊗Q:
0 /d47/d47 (P ⊗A) ⊕ (Q ⊗A)
πA
/d15/d15
1⊗f ⊕1⊗f/d47/d47 (P ⊗B) ⊕ (Q ⊗B)
πB
/d15/d15
1⊗g⊕1⊗g/d47/d47 (P ⊗C) ⊕ (Q ⊗C)
πC
/d15/d15
/d47/d47 0
0 /d47/d47P ⊗A
1⊗f /d47/d47P ⊗B
1⊗g /d47/d47P ⊗C /d47/d47 0,
whereπA is the projection along Q ⊗A toP ⊗A, etc. As these projections are
surjective we see the diagram commutes. Now we will use the exactness of the
ﬁrst row to deduce the exactness of the second row – we diagram chase.
Takea ∈Ker 1 ⊗f . Since πA is epic, there exists a a′ ⊕a′′ which maps to
a via πA. Likewise, there exists a 0 ⊕b in the pre-image of 0 via πB since it is
projection to P ⊗B along Q ⊗B. Since the diagram commutes we see:
a′ ⊕a′′ /d31(1⊗f )⊕(1⊗f ) /d47/d47/d95
/d15/d15
0 ⊕b/d95
/d15/d15
a /d31 1⊗f /d47/d47 0
But (1 ⊗f ) ⊕ (1 ⊗f ) is monic so a′ = 0 and so a = 0, and so 1 ⊗f is monic.
Now take anyc ∈P ⊗C. Since πC is surjective it follows there exists a c′ ⊕c′′
such that πC(c′ ⊕c′′) = c. Recall that the top row is exact so (1 ⊗g) ⊕ (1 ⊗g) is
epic and so there exist a b′ ⊕b′′ which coversc′ ⊕c′′. But now we simply project
the element to b via πB and as the diagram commutes we see b coversc:
b′ ⊕b′′ /d31 (1⊗g)⊕(1⊗g) /d47/d47/d95
/d15/d15
c′ ⊕c′′
/d95
/d15/d15
b /d31 1⊗g /d47/d47c

Algebra – James Wilson 119
Now we must show the sequence is exact at B. So ﬁrst is Im 1 ⊗f ≥
Ker 1 ⊗g? Take any b ∈ Ker 1 ⊗g. Since this maps to 0 via 1 ⊗g we may
pullback to 0 in ( P ⊗C) ⊕ (Q ⊗C) with πC. Next we use the exactness of
the top row to assert the existence of b′ which maps to b via πB and to 0 via
(1 ⊗g) ⊕ (1 ⊗g). Thus the exactness in the top row gives the existence of an
a′ that maps to b′ and if we project this using πA we get an a that maps to b
which maps to 0. Therefore, every element in the Ker 1 ⊗g is contained in the
image of 1 ⊗f .
a′ /d31 5 /d47/d47/d95
6
/d15/d15
b′ /d31 3 /d47/d47/d95
4
/d15/d15
0/d95
2
/d15/d15
a /d31 7 /d47/d47b /d31 1 /d47/d47 0
Now take any a ∈P ⊗A and consider its image b = (1 ⊗f )(a). This element we
retract alongπB to someb′ which intern we see is in the image of (1 ⊗f )⊕(1⊗f )
by retracting a along πA and using the commutativity of the square. Thus b′
maps to 0 over the tensor of g, and so its projection also maps to 0 proving
Im 1 ⊗f ≤Ker 1 ⊗g. Unfortunately the resulting diagram chase is identical
and not enlightening:
a′ /d31 3 /d47/d47/d95
4
/d15/d15
b′ /d31 5 /d47/d47/d95
2
/d15/d15
0/d95
6
/d15/d15
a /d31 1 /d47/d47b /d31 7 /d47/d47 0
In the end we agree the second row is exact and so indeed projective modules
are ﬂat. □
128 Induced Quotient Modules Hint: Use the universal prop-
erty of tensors.
(i) IfI is a right ideal of R andV is a left R-module, then there is an isomor-
phism of abelian groups
R/I ⊗RV ∼=V/IV,
where IV is the subgroup of V generated by all elements xv with x ∈ I,
v ∈V .
(ii) If R is a commutative and I, J are ideals in R, then R/I ⊗R R/J ∼=
R/(I +J).
Proof:
(i) Deﬁne the map f : R/I ×R V → V/IV on the pure tensors as: f (r +
I,v ) = rv +IV . That f is well-deﬁned follows from r +I =s +I implies
rv −sv +IV = (r −s)v +IV =IV . Moreover,
f ((r +I)s,v ) = f (rs +I,v ) = rsv +IV =f (r +I,sv );
f ((r +I) + (s +I),v ) = f ((r +s) +I,v ) = (rv + +IV ) + (sv +IV )
= f (r +I,v ) +f (s +I,v );
f (r +I,v +w) = ( rv +IV ) + (rw +IV ) = f (r +I,v ) +f (r +I,w ).
Therefore f is R-balance so it induces a map f from the tensor to V/IV .
Now we must build an inverse map and we will conclude this map is an
isomorphism.

120 CHAPTER 3. MODULES
Takeg : V/IV → R/I ⊗RV to be v +IV ↦→ (1 +I) ⊗v, and of course
generalize linearly. First take v +IV = v′ +IV so that v −v = iw for
some w ∈V , and i ∈I. Then
g(0) = g((v +IV ) − (v′ +IV )) = (1 +I) ⊗v −v′ = (1 +I) ⊗iw =I ⊗w = 0.
Therefore g is well-deﬁned. Now
f (g(v +IV )) = f ((1 +I) ⊗v)) = f ((1 +I) ⊗v) = v +IV.
Likewise
g(f (((r+I)⊗v)) = g(f ((r+I)⊗v)) = g(rv+IV ) = (1+I)⊗rv = (r+I)⊗v.
So f is bijective so it is an isomorphism.
(ii) Consider I(R/J ). Given i(r +J) = ir +iJ = i′ +J where i′ = ir in I
– which exists because I is an ideal, and J absorbs the i as well because
it is an ideal. Therefore I(R/J ) ≤ I +J/J . Now let r = 1 and notice
i(1 +J) = i +J and so indeed I +J/J ≤I(R/J ) so I +J/J =I(R/J ).
Now we notice by the third isomorphism theorem and our work in part (i)
that:
R/I ⊗RR/J ∼= R/J
I(R/J ) = R/J
(I +J)/J =R/(I +J).
□
129 Tensored Maps – True or False? If f :V →V ′ and g :W →W ′ areHint: Consider covering all
pure tensors ﬁrst. surjective maps of right and left R-modules respectively, thenf ⊗g is surjective.
Proof: True. Take a pure tensor v′ ⊗w′ ∈V ′ ⊗W ′. As f andg are surjective
there exists a pure tensor v ⊗w ∈V ⊗W such that f (v) ⊗g(w) = v′ ⊗w′. So
f ⊗g is surjective on pure tensors. However pure tensors generate V ′ ⊗W ′ so
f ⊗g is surjective. □
130 Endomorphism Rings and Tensors LetR be a commutative ring andHint: Use the universal prop-
erty of tensors to construct the
maps.
V andW beR-modules. Show that there exists a homomorphism of R-algebras
θ :EndR(V ) ⊗REndR(W ) →EndR(V ⊗W )
where
θ(f ⊗g)(v ⊗w) = f (v) ⊗g(w),
for all v ∈V , w ∈W , f ∈EndR(V ) and g ∈EndR(W ).
Proof: First observe that both V andW are bi-modules so indeed RVR ⊗RW
is an R-module and EndR(V ) = HomR(RVR,RV ) is an R-module as well as a
ring, so indeed all objects concerned are R-algebras. Now we construct θ from
the universal mapping property for tensors.
Let Θ : EndR(V ) ×EndR(W ) →EndR(V ⊗W ) be given by
Θ(f,g ) = f ⊗g.
As there are no equivalence classes we are assured this is well-deﬁned and clearly
f ⊗g :V ⊗W →V ⊗W ∈EndR(V ⊗W ). Now we check if Θ is middle linear.
Θ(f +h,g )(v ⊗w) = (( f +h) ⊗g)(v ⊗w) = (f +h)(v) ⊗g(w) = f (v) +h(v) ⊗g(w)
= f (v) ⊗g(w) +h(v) ⊗g(w) = (f ⊗g)(v ⊗w) + (h ⊗g)(v ⊗w)
= (( f ⊗g) + (h ⊗g))(v ⊗w) = (Θ(f,g ) + Θ(h,g ))(v ⊗w);
Θ(fr,g )(v ⊗w) = ( fr ⊗g)(v ⊗w) = f (v)r ⊗g(w) = f (v) ⊗rg(w)
= ( f ⊗rg)(v ⊗w) = Θ(f ⊗rg)(v ⊗w).

Algebra – James Wilson 121
Of course the sum in the right component is completely symmetric. Therefore
Θ is middle linear so it induces the map θ which we see agrees with the stated
deﬁnition. □
131 Induced Modules over Tensors Suppose f : R → S is a surjective Hint: The obvious R-module
structure is well-deﬁned be-
cause of the partition induced
by the surjection. Use the uni-
versal property of tensors for
the rest.
ring homomorphism. Let V and W be right and left S-modules respectively.
Describe how to give V and W a right and left R-module structure and prove
V ⊗RW ∼=V ⊗SW.
If f is not surjective, is V ⊗RW ∼=V ⊗SW ?
Proof: Let r ∈ R and v ∈ V , w ∈ W . Then deﬁne r ·v = f (r)v and
r ·w =f (r)w. Since f (r) ∈S it is clear that the extension to R is well-deﬁned.
To verify this is an R-module notice:
(r +s) ·v = f (r +s)v =f (r)v +f (s)v =r ·v +s ·v;
(rs) ·v = ( f (r)f (s))v =r · (f (s)v) = r · (s ·v);
r · (v +v′) = f (r)(v +v′) = f (r)v +f (r)v′ =r ·v +r ·v′.
Now we construct the isomorphism by using the universal property of ten-
sors. Let g :V ×W →V ⊗SW be given by g(v,w ) = v ⊗w. Given any r ∈R
we have:
g(vr,w ) = vf (r) ⊗w =v ⊗f (r)w =g(v,rw )
g(v +u,w ) = ( v +u) ⊗w =v ⊗w +u ⊗w =g(v,w ) +g(u,w ).
Therefore we have an induced map g :V ⊗RW →V ⊗SW . For the reverse map
we again use the universal property, but the design is a canonical embedding so
the R-balance is clear: h(v ⊗w) = v ⊗w. Clearly the two maps are inverses
and so they are an isomorphism of abelian groups. □
Example: No. Let R = Z andS = Z ⊕ Z withf the inclusion map 1 ↦→ (1, 0).
Recall
Z ∼=Z ⊗Z⊕Z Z ⊕ Z ≇ Z ⊗Z Z ⊕ Z ∼= Z ⊕ Z.
□
132 Dimension and Tensors – True or False? IfV andW are respectively Hint: dimDA ⊗ B =
dimDAdimDB.right and left D-modules, for a division algebra D, such that V ⊗DW = 0, then
either V = 0 or W = 0.
Proof: True. First recall that modules over a division ring are vector spaces,
and as such are free and have well-deﬁned dimension. Also recall
dimD(V ⊗DW ) = dimDV ·dimDW
even if we consider inﬁnite cardinalities (here 0 times inﬁnity is 0.) Hence
0 = dimD0 =dimDV ⊗DW =dimDV ·dimDW
which implies dimDV = 0 or dimDW = 0. Since vector spaces are free, this
implies one of the two modules is trivial. □
133 Annihilating Modules – True or False? Let R be a commutative Hint: Consider the case when
all simple modules are torsion
modules.
ring and V be an R-module. If L ⊗RV = 0 for every simple R-module L then
V = 0.

122 CHAPTER 3. MODULES
Example: False. Consider R = Z andV = Q. We know each simple R-module
to be Z/p for some prime p. However
Z/p ⊗Z Q = 0.
But clearly Q ⁄= 0. □
134 Identity Tensor – True or False? Let V be a left R-module. IfHint: Consider letting X =
R.
X ⊗RV ∼= 0
for all right R-modules X, then V ∼= 0.
Proof: True. Let X =RR. Then we have two results which in the end prove
our question:
0 ∼=RR ⊗RV ∼=V.
□
135 Tensors over Free Modules – True or False? If V , V1, and V2 areHint: Tensors distribute over
the components of free mod-
ules, so a rank formula exists.
non-trivial free R-modules over a commutative ring R, where each is ﬁnitely
generated and V ⊗RV1 ∼=V ⊗RV2 then V1 ∼=V2.
Proof: True. Notice that
rankRV ·rankRV2 =rankRV ⊗RV1 =rankRV ⊗RV2 =rankRV ·rankRV2.
As every term is ﬁnite, and non-zero, it follows by cancellation in the integers
that rankRV1 =rankRV2. Any two free modules of the same rank are isomor-
phic, so V1 ∼=V2. □
136 Applied Tensors – True or False? Z3 ⊗Z (Z ⊗Z Z2) ∼= Z6.Hint: Use Exercise- 3.121.
Example: False.
Z3 ⊗Z (Z ⊗Z Z2) ∼= Z3 ⊗Z Z2 ∼= 0.
□
137 Applied Tensors – True or False? Find ( Q ⊕ Z7) ⊗Z Z5.Hint: Use Exercise- 3.121.
Example:
(Q ⊕ Z7) ⊗Z Z5 ∼= (Q ⊗ Z5) ⊕ (Z7 ⊕ Z5) = 0.
□
138 Applied Tensors – True or False? True or False: Z35 ⊗Z Z5 ∼= Z7?Hint: Use Exercise- 3.121.
Example: False.
Z35 ⊗Z Z5 ∼= Z5.
□
139 Applied Tensors – True or False? Find ( C ⊕ Z6) ⊗Z Z3.Hint: Use Exercise- 3.121.
Example:
(C ⊕ Z6) ⊗Z Z3 ∼= (C ⊗ Z3) ⊕ (Z6 ⊕ Z3) = Z3.
□
140 Quotients and Tensors – True or False? LetR be a ring, V a right R-Hint: Prove using the univer-
sal property of tensors directly.

Algebra – James Wilson 123
module, and W a left R-module. Then the additive group V ⊗RW is a quotient
of the abelian group V ⊗ZW .
Proof: True. It is suﬃcient to construct a surjection from V ⊗ZW toV ⊗RW .
To do this we follow the universal property: f (v,w ) = v ⊗Rw. This is a well-
deﬁned map as it is the canonical middle linear map for V ⊗RW ; however, it
may not be Z-balanced. However recall that Z/m ≤ R where char R = m –
possibly 0. So we can say for any n ∈ Z thatv ·n ∈V as we take n to act on v
as n +mZ. Thus
f (vn,w ) = vn ⊗w =v ⊗nw =f (v,nw ).
It is clear that f is R-balanced so sums follow as required. Therefore f is Z-
balanced. Thus we have f :V ⊗ZW →V ⊗RW which is clearly surjective as it
is surjective on the pure tensors – the generators of these two abelian groups. □
141 Mixed Ring Tensors Give an example of a ring R,V a right R-module Hint: Consider R = Z ⊕ Z.
and W are left R-module such that V ⊗RW ≇V ⊗ZW as abelian groups.
Example: Let R = Z ⊕ Z. Then
Z ⊕Z⊕Z Z ⊕ Z = Z; Z ⊕Z Z ⊕ Z = Z ⊕ Z.
□
142 Fields and Tensors – True or False? IfK/Q andL/Q are ﬁnite ﬁeld Hint: Use the dimension rule
to conclude the extension is ﬁ-
nite.
extensions then K ⊗QL is a semi-simple artinian ring.
Proof: True.
As dimQK ⊗Q L = dimQKdim QL we see that as a vector space K ⊗Q L
is ﬁnite dimensional. Therefore it is trivially artinian as a Q-algebra. Also we
note that given a ⊗b,c ⊗d ⁄= 0 then ac ⊗bd ⁄= 0 as ac ⁄= 0 and bd ⁄= 0 and both
K and L have no zero-divisors.
□

124 CHAPTER 3. MODULES

Chapter 4
Categories
5 . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 126
125

126 CHAPTER 4. CATEGORIES
5 If the functors F : A → B and G : B → A establish an equivalence of
categories between A and B then F is both left and right adjoint to G.
Proof: Let
FA
α
/d15/d15
Ff /d47/d47FA ′
α
/d15/d15
A
/d125/d125/d124/d124/d124/d124/d124/d124/d124/d124
/d97/d97/d66 /d66 /d66 /d66 /d66 /d66 /d66 /d66 f /d47/d47A′
/d34/d34/d69/d69/d69/d69/d69/d69/d69/d69
/d60/d60/d121/d121/d121/d121/d121/d121/d121/d121
GA Gf
/d47/d47GA′.
□

Chapter 5
Rings
1 T/F Jacobson Radical . . . . . . . . . . . . . . . . . . . . 129
2 Jacobson Radical . . . . . . . . . . . . . . . . . . . . 129
3 Primary Ideals . . . . . . . . . . . . . . . . . . . . . 129
4 Primary Containment . . . . . . . . . . . . . . . . . 129
5 Primary Decomposition . . . . . . . . . . . . . . . . 130
6 Maximal Radicals . . . . . . . . . . . . . . . . . . . . 130
7 Associated Primes . . . . . . . . . . . . . . . . . . . 130
8 Localization . . . . . . . . . . . . . . . . . . . . . . . 130
9 Localization . . . . . . . . . . . . . . . . . . . . . . . 131
10 T/F Localized Local Rings . . . . . . . . . . . . . . . . . 131
11 Localization of Primes . . . . . . . . . . . . . . . . . 131
12 T/F Primary Ideals . . . . . . . . . . . . . . . . . . . . . 132
13 Local Rings . . . . . . . . . . . . . . . . . . . . . . . 132
14 Nil-Radical . . . . . . . . . . . . . . . . . . . . . . . 132
15 T/F Polynomial Rings . . . . . . . . . . . . . . . . . . . . 132
16 T/F Noetherian Rings . . . . . . . . . . . . . . . . . . . . 132
17 T/F Artinian Rings . . . . . . . . . . . . . . . . . . . . . 132
18 T/F UFDs . . . . . . . . . . . . . . . . . . . . . . . . . . 133
19 T/F Noetherian Rings . . . . . . . . . . . . . . . . . . . . 133
20 T/F Noetherian PIDs . . . . . . . . . . . . . . . . . . . . 133
21 T/F Prime Ideals . . . . . . . . . . . . . . . . . . . . . . . 133
22 T/F Prime Ideals . . . . . . . . . . . . . . . . . . . . . . . 133
23 T/F UFDs . . . . . . . . . . . . . . . . . . . . . . . . . . 133
24 T/F Prime Intersection . . . . . . . . . . . . . . . . . . . 134
25 T/F Tensors . . . . . . . . . . . . . . . . . . . . . . . . . 134
26 T/F Prime Ideals . . . . . . . . . . . . . . . . . . . . . . . 135
27 Primary Ideals . . . . . . . . . . . . . . . . . . . . . 135
28 Units . . . . . . . . . . . . . . . . . . . . . . . . . . . 135
29 T/F Localization of Ideals . . . . . . . . . . . . . . . . . . 135
30 T/F Localization and Radicals . . . . . . . . . . . . . . . 136
31 Localization . . . . . . . . . . . . . . . . . . . . . . . 136
32 Localization of Domains . . . . . . . . . . . . . . . . 136
33 Localized Modules . . . . . . . . . . . . . . . . . . . 137
34 Integral Fields . . . . . . . . . . . . . . . . . . . . . . 137
35 T/F Integral Closure . . . . . . . . . . . . . . . . . . . . . 137
36 T/F Integral Closure . . . . . . . . . . . . . . . . . . . . . 137
37 T/F Integral Closure . . . . . . . . . . . . . . . . . . . . . 137
127

128 CHAPTER 5. RINGS
38 Integral Closure . . . . . . . . . . . . . . . . . . . . . 137
39 Idempotent Ideals . . . . . . . . . . . . . . . . . . . . 137
40 T/F Finite Local Rings . . . . . . . . . . . . . . . . . . . 138
41 T/F Local Artinian Rings . . . . . . . . . . . . . . . . . . 138
42 Primary Decomposition . . . . . . . . . . . . . . . . 138
43 Algebraic Extensions . . . . . . . . . . . . . . . . . . 139
44 Integrality of Polynomials . . . . . . . . . . . . . . . 139
45 Integral Closures and Polynomials . . . . . . . . . . 139
46 Integrality . . . . . . . . . . . . . . . . . . . . . . . . 139
47 Integral Closure over Z . . . . . . . . . . . . . . . . . 140
48 Integral Closure of Non-UFDs . . . . . . . . . . . . . 141
49 Prime Ideals of Integral Extensions . . . . . . . . . . 141
50 Prime Unions . . . . . . . . . . . . . . . . . . . . . . 142
51 Primary Decomposition . . . . . . . . . . . . . . . . 142
52 Prime Height . . . . . . . . . . . . . . . . . . . . . . 142
53 Krull Dimension . . . . . . . . . . . . . . . . . . . . 142
54 Krull Dimension . . . . . . . . . . . . . . . . . . . . 143
55 Minimal Primes . . . . . . . . . . . . . . . . . . . . . 143
56 T/F Generators of Varieties . . . . . . . . . . . . . . . . . 144
57 T/F Non-radical Ideals . . . . . . . . . . . . . . . . . . . 144
58 T/F Ideal Lattice and Varieties . . . . . . . . . . . . . . . 144
59 T/F Radical Ideals . . . . . . . . . . . . . . . . . . . . . . 144
60 Direct Products with Varieties . . . . . . . . . . . . 144
61 T/F DCC for Varieties . . . . . . . . . . . . . . . . . . . . 145
62 T/F ACC for Varieties . . . . . . . . . . . . . . . . . . . . 145
63 T/F ACC for Varieties . . . . . . . . . . . . . . . . . . . . 145
64 T/F Solution Sets and Varieties . . . . . . . . . . . . . . 145
65 T/F Zariski Topology . . . . . . . . . . . . . . . . . . . . 146
66 Zariski Topology . . . . . . . . . . . . . . . . . . . . 146
67 T/F Zariski Topology and Frobenius . . . . . . . . . . . . 147
68 Automorphisms of Varieties . . . . . . . . . . . . . . 147
69 Isomorphism of Varieties . . . . . . . . . . . . . . . . 147

Algebra – James Wilson 129
1 Jacobson Radical – True or False? J(R[x]) = 0. Hint: Consider irreducible
polynomials and there associ-
ated maximal ideals.
Proof: True. As we have a commutative ring, maximal left ideals are two-
sided ideals. The maximal ideals of R[x] are those generated by irreducible
polynomials (as R[x] is a PID).
Given the irreducible polynomials x−n forn ∈ Z it follows each In = (x−n)
is a distinct maximal ideal of R[x]. Also, ∩n∈ZIn = (p(x)) since R[x] is a PID.
Yet this requires x −n|p(x) for all n ∈ Z. Unfortunately no polynomial has
inﬁnitely many roots so no such p(x) exists save p(x) = 0. Since J(R[x]) is at
least contained in this intersection we must conclude that J(R[x]) = 0. □
2 Jacobson Radical Let R = R[[x]]. Calculate J(R) and Rad R. Hint: R[[x]] is an integral do-
main.Example: Since R[[x]] is a local ring it follows J(R) = (x). Moreover, R is an
integral domain, so R[[x]] is an integral domain; thus, there are no zero-divisors,
let alone nilpotent elements. Hence, Rad R= 0. □
3 Primary Ideals The ideal (4, 2x,x 2) in Z[x] is primary but not irreducible. Hint: Show the quotient has
no non-nilpotent zero-divisors.Proof: Let I = (4, 2x,x 2) and notice
(4)< (4,x 2)< (4,x 2, 2x).
Thus by the third isomorphism theorem we get:
R = Z[x]/(4,x 2, 2x) ∼= Z[x]/(4)
(4,x 2, 2x)/(4)
∼= Z4[x]/(x2)
(x2, 2x)/(x2).
Thus
R = {0 +I, 1 +I, 2 +I, 3 +I,x +I, (x + 1) +I, (x + 2) +I, (x + 3) +I}.
Now we simply check that all zero-divisors are nilpotent. First notice the ele-
ments 1 +I, 3 + I, (x + 1) +I, and (x + 3) +I are all units, indeed of order 2,
so they are not zero-divisors. Finally, 0 + I, 2 + I, x +I, and ( x + 2) + I are
all nilpotent of order 2, so all zero-divisors are nilpotent. Hence I is primary in
Z[x] – in particular it is (2 ,x )-primary, where (2,x ) is prime as its quotient is
the ﬁeld Z/2.
However as suggested I is not irreducible as visibly
(4, 2x,x 2) = (4,x ) ∩ (2,x 2).
[Z[x] is a UFD so intersections are generated by all all minimal products, i.e.:
(4, 4x2, 2x,x 2) = (4, 2x,x 2).] □
4 Primary Containment The ideal I = (x2, 2x) in Z[x] is not primary, but Hint: Show the quotient has
a non-nilpotent zero-divisor.(x2)<I < (x) and the ideal ( x) is prime, and ( x2) is (x)-primary.
Example: To show I is not primary it is suﬃcient to show that the quotient
contains some non-nilpotent zero-divisor. To do this observe that
x(x + 2) = x2 + 2x ≡ 0 (mod I)
yet
(x+2)m = (x+2)2(x+2)m−2 = (x2 +4x+4)(x+2)m−2 ≡ 4(x+2)m−2 (mod I)
So if (x + 2) is nilpotent mod I, then 4 is a zero-divisor mod I and so would also
be nilpotent. However 4 i /∈I as x has no inverse in I, and so 4 is not nilpotent

130 CHAPTER 5. RINGS
so either it is not a zero-divisor in which case ( x + 2) is a criminal element, or
it is itself a non-nilpotent zero-divisor. In either event, I is not primary.
That (x) is primary follows from that fact that Z[x]/(x) = Z which is an
integral domain. That ( x2) is ( x)-primary follows from the fact that for all
ab ∈ (x2) where a /∈ (x2) we see x2|ab so x2 ∤ a so x|b for certain b ∈ (x) and√
(x2) = (x). □
5 Primary Decomposition Represent the ideal (9 , 3x + 3) in Z[x] as theHint: Recall that Z[x] is a
UFD so irreducible factors are
immutable.
intersection of primary ideals.
Example: Since Z is a UFD so is Z[x]. Thus intersections can be detected by
divisors. Consider the intersection (3) ∩ (9,x + 1). Any element in the intersec-
tion must be divisible by 3, and furthermore also by either 9 or by x + 1. In the
ﬁrst case then the element is simply divided by 9, so indeed we must include
the minimal version of such an element – 9 itself. In the later case as 3( x + 1)
divides the element, then 3 x + 3 must be in the intersection as well. Given any
element in the intersection it is characterized by being divided by either 9 or
3x + 3 thus the intersection is precisely (9 , 3x + 3). □
6 Maximal Radicals Let I be an ideal of a commutative ring R such thatHint: Pass to R/I and notice√
I/I is now the nil-radical of
R/I.
√
I is a maximal ideal in R. Prove that I is primary.
Proof: Given that
√
I is a maximal ideal we see that in R/I,
√
I/I is also
a maximal ideal. Given any x +I which is nilpotent, it follows xn +I = I so
xn ∈I and we now see that
√
I/I is precisely the nil-radical of R/I. So it is the
intersection of all prime ideals in R/I. Yet this implies, by the maximality of√
I/I , that
√
I/I is the only prime ideal in R/I, so also the only maximal ideal
inR/I. Hence R/I is a local ring and indeed
√
I/I must contain all non-units.
In particular, all zero-divisors. However, moments ago we notice,
√
I/I is the
nil-radical so it contains nothing but the nilpotent elements of the ring R/I so
is follows all zero-divisors of R/I are nilpotent, and so this characterizes I as a
primary ideal in R. □
7 Associated Primes In a noetherian ring, prove that
√
I is the intersectionHint: Notice
√
I ∩J =
√
I ∩√
J. of the associated prime ideals of I.
Proof: Let
I =Q1 ∩ · · · ∩Qn
be an irredundant primary decomposition of I, with Pi = √Qi the associated
primes. These associated primes are uniquely determined in a noetherian ring
by the Lasker-Noether theorem.
It follows
√
I ∩J =
√
I ∩
√
J as given any xn ∈I ∩J clearly xn ∈I and J
so x ∈
√
I ∩
√
J, and the process is reversible.
Finally √
I =
√
Q1 ∩ · · · ∩Qn =
√
Q1 ∩ · · · ∩
√
Qn.
□
8 Localization Let S = Z×
m be the set of all units in Zm (equivalently theHint: Inverting the invertible
elements should not change
anything.
set of all non-zero-divisors,) and determine S−1Zm.
Example: Consider the equivalence relation: a
b = c
d if and only if for some
u ∈S we haveu(ad −bc) = 0. However, u is in S so by the choice of S,u is not
a zero-divisor, and hence we must have ad =bc. Hence
[r
s
]
=
{rt
st : t ∈S
}
.

Algebra – James Wilson 131
In particular, as all elements of S are units, each r/s can be expressed as r′/1.
Thus we see a canonical isomorphism between Zm and S−1Zm. □
9 Localization LetS be a multiplicative subset of R andT be a multiplicative Hint: Use the universal prop-
erty of localization.subset of S−1R. Let S∗ = {r ∈ R :
[r
s
]
∈ T for some s ∈ S}. Then
S∗ is a multiplicative subset of R and there is a ring homomorphism S−1
∗ R ∼=
T −1(S−1R).
Proof: Given any a,b ∈ S∗ it follows there exist s,t ∈ S for which a
s, b
t ∈ T .
This means st ∈ S as S is multiplicative and furthermore, ab
st ∈ T as T is
multiplicative. Therefore ab ∈S∗. Given that 1 ∈T , then for any s ∈S, s
s ∈T
provingS ⊆S∗ and so speciﬁcally 1 ∈S∗ provingS∗ is multiplicative itself.
Now deﬁne the map:
f :R →T −1(S−1R) : r ↦→ r/1
1/1
and we quickly verify this is an R-homomorphism. Through the universal prop-
erty we now get an S−1
∗ R-homomorphism
ˆf :S−1
∗ R →T −1(S−1R) : r
s ↦→ r/s
s/s′,
wheres′ ∈S is any such that s/s′ ∈T . By the universal property applied T we
get another map
ˆg :T −1(S−1R) →S−1
∗ R : r/s
t/s′ ↦→ rs′
st.
It follows routinely that fg =id and gf =id so this is an isomorphism. □
10 Localized Local Rings – True or False? If R is a local ring, then there Hint: Localize on the unique
maximal ideal.is a commutative ring R′ and a prime ideal P of R′ such that R ∼=R′
P .
Proof: Let P be the unique maximal ideal in R. As such, P contains all
non-units of R. Indeed, P is also prime as it is maximal. Thus letting R′ =R
we see that R′
P ∼=R. □
11 Localization of Primes Let p be a prime ideal of R. Show that Rp/pp Hint: Use the universal prop-
erty of localization.is isomorphic to the ﬁeld of quotients of R/p.
Proof: Deﬁne a map f :R →Fr (R/p) as f (r) = [r + p/1 + p]. This deﬁnition
makes sense as it is simply the composition of the canonical projection map
R → R/p followed by the canonical inclusion map R/p → Fr (R/p), and thus
there is no need to verify f is an R-algebra homomorphism. More importantly,
we see given any s /∈ p, f (s) ⁄= 0 so f (s) is invertible. Thus we have from the
universal property of localization the following:
R
µ /d47/d47
f
/d35/d35/d72/d72/d72/d72/d72/d72/d72/d72/d72 Rp
ˆf
/d15/d15
Fr (R/p).
Given any [r + p/s + p] ∈Fr (R/p)
[r + p
s + p
]
=
[r + p
1 + p
][s + p
1 + p
]−1
=f (r)f (s)−1 = ˆf ([r]p) ˆf ([s]p)−1 = ˆf
([r
s
]
p
)
.

132 CHAPTER 5. RINGS
Hence ˆf is surjective. Now we inspect the kernel.
Given [r/s]p in the kernel of ˆf it follows [ f (r)/f (s)] = [0 /1] in Fr (R/p).
Hence f (r) = 0 and so r ∈ Ker f. This implies r ∈ p since the kernel of f
is determined entirely by the projection of R → R/p. Hence [ r/1]p ∈ pp and
since pp is and ideal it follows that in fact [ r/s]p is contained in pp. Therefore
the kernel of ˆf is contained in pp. It is not diﬃcult to see the reverse of this
inclusion as well. So we conclude that the kernel of our map is precisely pp and
so by the ﬁrst isomorphism theorem we have
Rp/pp ∼=Fr (R/p).
□
12 Primary Ideals – True or False? The ideal (x2, 4) is (x, 2)-primary inHint: Show (x, 2) is a maxi-
mal ideal and invoke Exercise-
5.6.
Z[x].
Proof: True. Clearly
√
(x2, 4) contains (x, 2), and since the quotient Z[x]/(x, 2) =
Z/2 it is clear that ( x, 2) is prime and indeed maximal so it must be the radi-
cal. Now we appeal to the fact of Exercise- 5.6 that all ideals whose radicals are
maximal are primary to this radical. □
13 Local Rings Let R be a noetherian local ring with maximal ideal MHint: Use Nakayama’s
Lemma. and let x1,...,x n ∈M . Suppose that {x1 +M 2,...,x n +M 2} is a basis of the
R/M-vector space M/M 2. Show that M =Rx1 + · · · +Rxn.
Proof: First notice since M is and ideal of R that M 2 is also an ideal. Thus
we have M/M 2 as an ideal of R/M2 and so M/M 2 is an R/M2-module. Thus
we are free to take the quotient module ( M/M 2)/(M ·M/M 2) = M/M 2 as and
R/M-module. So the question makes sense.
TakeN =Rx1 +· · ·+Rxn which is clearly contained in M . As this is a basis
for M/M 2 as an R/M-module, it follows M =N +M 2 =N +MM . However
R is a local ring so J(R) = M . This means we have the setup of Nakayama’s
lemma: M =N +J(R)M and so M =N . We see M =R. □
14 Nil-Radical Let R be a commutative ring with a unique prime ideal PHint: P must be the nil-
radical. and let r ∈R. Prove that x is nilpotent if and only if x ∈P .
Proof: Since R has only one prime ideal then Rad R = P so P contains all
nilpotent elements and indeed is all nilpotent elements. □
15 Polynomial Rings – True or False? C[x,y ] is a PID.Hint: Consider (x,y ).
Example: False. Consider the ideal ( x,y ). Since C[x,y ]/(x,y ) ∼= C it follows
(x,y ) is a proper maximal ideal and thus prime. Now we must make sure it is
not principal.
Suppose (p(x,y )) = (x,y ). Then x|p(x,y ) and y|p(x) so indeed xy|p(x,y ).
However it follows then that x = q(x)p(x,x ) for some q(x) in C[x]. Yet as
xy|p(x,y ) it follows x2|p(x,x ) so by a degree argument we see we reach a con-
tradiction. Hence ( x,y ) is not principal. □
16 Noetherian Rings – True or False? C[x,y ] is a noetherian ring.Hint: Use the Hilbert Basis
Theorem. Proof: True. By the Hilbert basis theorem any polynomial ring over a noethe-
rian ring is noetherian. Hence C[x] is noetherian and so also C[x][y] = C[x,y ].
□

Algebra – James Wilson 133
17 Artinian Rings – True or False? Every subring of an artinian ring isHint: Consider Q.
artinian.
Example: False. Since Q is a ﬁeld it is artinian. However it clearly contains
the non-artinian ring Z which has an inﬁnite descending chain
(2)> (4)> (8)> · · ·.
□
18 UFDs – True or False? Z[x] is a UFD. Hint: Polynomials over UFDs
are UFDs.Proof: True. Since Z is a PID it is also a UFD, and as polynomial rings over
a UFD are a UFD we see indeed Z[x] is a UFD. □
19 Noetherian Rings – True or False? Z[x,y ]/(x − 2y) is a noetherian Hint: Quotients of noetherian
Rings are noetherian.ring.
Proof: True. As Z is noetherian, the Hilbert basis theorem tells us so is Z[x,y ].
We also no quotients of noetherian rings are noetherian by the correspondence
theorem. So Z[x,y ]/(x − 2y) is noetherian. □
20 Noetherian PIDs – True or False? If R is a PID then R is noetherian. Hint: Every non-zero non-
unit in R has a ﬁnite unique
factorization into primes.
Proof: Given any chain of principal ideals
0< (r1) ≤ (r2) ≤ · · · .
It follows ri|ri−1| · · · |r2|r1. However in a PID we may factor r1 ⁄= 0 into a ﬁnite
unique set of irreducibles with diﬀerence only by a unit. So unless ri = rj for
alli<j for suﬃciently large i, we will run out of irreducibles to eliminate from
r1. Thus the chain stabilizes in ﬁnitely many steps. □
21 Prime Ideals – True or False? If R is a noetherian ring then every Hint: Consider C[x,y ].
non-zero prime ideal of R is maximal.
Example: False. Consider C[x,y ]. By the Hilbert basis theorem this is a
noetherian ring. Furthermore, ( x)< (x,y ) and both are prime since their quo-
tients give the integral domains C[y] and C respectively. However visibly ( x) is
not maximal. □
22 Prime Ideals – True or False? IfR is a UFD then every non-zero prime Hint: Consider C[x,y ].
ideal of R is maximal.
Example: False. Consider k[x,y ], with k any ﬁeld. Since k is a ﬁeld it is a
PID and so also a UFD. Hence k[x] is a UFD so indeed k[x][y] = k[x,y ] is a
UFD. Notice k[x,y ]/(y) ∼= k[x] which is an integral domain so ( y) is a prime
ideal. Yet k[x] is not a ﬁeld as x has no inverse. □
23 UFDs – True or False? Hint: Use the subring Z[
√
10]
of R.(a) Every quotient ring of a UFD is a UFD.
(b) Every subring of a UFD is a UFD.
Example:
(a) False. Consider Z which is a PID and so also a UFD. The quotient Z/6Z is
not an integral domain so in particular it is not a UFD.

134 CHAPTER 5. RINGS
(b) False. Consider the ring R = {a +b
√
10 : a,b ∈ Z} as a subring of R.
Certainly the ﬁeld R is a UFD, but we need to verify R is not. Notice
2 · 3 = 6 = (4 +
√
10)(4 −
√
10).
Now we must verify that all these are irreducible. We do this in parts with
some tools.
(i) There exists a norm functionN :R → Z such thatN (xy) = N (x)N (y),
and N (x) = 0 if and only if x = 0.
(ii) N (u) = ±1 if and only if u is a unit in R.
(i) Deﬁne the norm of an element x = a +b
√
10 to be xx where x =
a −b
√
10, so that N (x) = a2 − 10b2 ∈ Z. Let x = a +b
√
10 and
y =c +d
√
10 be arbitrary elements of R.
N (xy) = N ((ac + 10bd) + (ad +bc)
√
10) = (ac + 10bd)2 − 10(ad +bc)2
= a2c2 + 100b2d2 − 10a2d2 − 10b2c2 = (a2 − 10b2)(c2 − 10d2)
= N (x)N (y).
Whenx = 0 it is clear N (x) = 0. Given N (x) = 0 it follows a2−10b2 =
0; therefore,a2 = 10b2 and so |a| = |b|
√
10. So either a is not an integer
or b is not, unless both are zero; so x = 0. Hence, N (x) = 0 if and
only if x = 0.
(ii) Supposeuv = 1 for two elementsu,v inR. Applying the norm function
it is clear N (u)N (v) = N (uv) = N (1) = 1. Since N maps only into
the integers and only 1 and −1 have multiplicative inverses in Z it
followsN (u) = ±1.
Now we may prove that the elements are irreducible. Suppose 2 = uv for
two non-units u andv inR. Then N (u)N (v) = N (2) = 4 and with u andv
being non-units it is forced that N (u) = ±2. Let u =a +b
√
10 and consider
the equation a2 − 10b2 = N (u) = ±2. Since the equation is true in the
integers it must be true in its factor rings; therefore, a2 − 10b2 ≡ 2 (mod 5).
However no element exists in Z/5Z such that a2 = 2 (proved by testing all
ﬁve elements.) So no u exists in R with the property N (u) = ±2 concluding
by contradiction that 2 is irreducible in R.
Again suppose 3 = uv with u and v again non-unit elements. Picking up
the pace suppose a2 − 10b2 =N (u) = ±3. Then a2 − 10b2 ≡ 3 (mod 5) but
once again a2 ⁄= 3 mod 5 for any elements a. Therefore 3 is irreducible in
R.
Finally N (4 ±
√
10) = 16 − 10 = 6. Suppose 4 ±
√
10 = uv for non-units
u and v. Then clearly N (u)N (v) = 6 and thus N (u) = ±2 or ±3 however
from the above argument it is clear no such element exists therefore 4 ±
√
10
is irreducible.
□
24 Prime Intersection – True or False? The intersection of prime ideals inHint: Consider Z.
a commutative ring is prime.
Example: False. Consider Z where primes correspond precisely to maximal
ideals pZ where p is a prime number. Here
2Z ∩ 3Z = 6Z

Algebra – James Wilson 135
which is not prime. □
25 Tensors – True or False? If R is a local ring with maximal ideal M Hint: Consider V ≤M .
and V is a ﬁnitely generated R-module with (R/M) ⊗RV = 0 then V = 0.
Example: False. Let R = C[[x]] and take M = V = (x). Certainly V is a
ﬁnitely generated R module, and R is also a local ring. Furthermore, R/M ⊗R
V ∼= 0 since
a(x) +M ⊗b(x)x =a(x)x +M ⊗b(x) = M ⊗Rb(x) = 0 + M ⊗b(x) = 0.
HoweverV ⁄= 0. □
26 Prime Ideals – True or False? If R is an integral domain and r ∈R is Hint: Work in ring which is
not a UFD.an irreducible element of R, then (r) is a prime ideal of R.
Example: False. Refer back to the example in Exercise-23. Here R was taken
to be Z[
√
10]. Recall
2 · 3 = 6 = (4 +
√
10)(4 −
√
10).
Suppose 2 is prime. Then R/(2) = Z + Z
√
10 has a nilpotent element
√
10 as
(
√
10)2 = 10 ≡ 0 (mod 2) .
Therefore we do not have an integral domain in the quotient so 2 is not prime. □
27 Primary Ideals Show that if Q is a primary ideal in a commutative ring Hint: Use the prime element
and division properties for the
converse.
R, then √Q is a prime ideal. Show the converse holds if R is a PID.
Proof: Considerab ∈ √Q. We wish to show a ∈ √Q orb ∈ √Q. Without loss
of generality let a /∈ √Q. Thus an /∈ Q for any n >0. However as ab ∈ √Q
it follows anbn = (ab)n ∈ Q for large enough n. Now using the deﬁnition of
primary we see that an /∈ Q implies bn ∈ √Q. But then bnm ∈ Q for some
m >0, so indeed b ∈ √Q – using the elemental deﬁnition of the radical ideal.
Therefore √Q is prime.
Now assume R is a PID and that √Q is prime for some ideal Q. We will
showQ is √Q-primary. As R is a PID there exists an element – a prime element
– p such that √Q = (p). Also take Q = (q). Then p√Q by deﬁnition implies
q|pn. But ( q) ≤ (p) implies p|q so q =pi for some i ≥ 0. Therefore Q = √Q
i
.
But any prime to a power is primary. □
28 Units Let R be an integral domain and F its ﬁeld of fractions. Then Hint:
r ∈R is a unit if and only if 1
r ∈F is integral over R.
Proof: Let r ∈R be a unit. It follows 1
r ∈R and so x − 1
r ∈R[x] so indeed 1
r
is integral over R.
Now suppose 1
r ∈F is integral overR. Then there exists a monic polynomial
p(x) = xn + · · · +a0 ∈R[x] such that p(1/r) = 0. That is:
1
rn + · · · + a1
r +a0 = 0;
1
r + · · · +a1rn−2 +a0rn−1 = 0
1
r = −an−1 −an−2r − · · · −a0rn−1 ∈R.
□

136 CHAPTER 5. RINGS
29 Localization of Ideals – True or False? LetS be a proper multiplicative Hint: Consider localizing at
an ideal which does not con-
tain I orJ.
subset of a commutative ring R andI ⁄=J be ideals of R. Then S−1I ⁄=S−1J.
Example: False. Let R = Z and I = 3 Z and J = 5 Z. Clearly I ⁄= J. Now
consider p = 2Z and localize over p. Thus Ip =Rp =Jp as we now have both 3
and 5 as units. □
30 Localization and Radicals – True or False? Let S be a properHint: Expand and contract
the intersection of prime ide-
als over I.
multiplicative subset of a commutative ring R and I be an ideal of R. Then√
S−1I =S−1√
I.
Proof: True. Let
√
I =⋂
I≤PP where P is a prime in R. If P is prime in R
then S−1P =R or S−1P is prime in S−1R. In particular when P avoidsS we
know S−1PC = P . So we see for every prime Q of S−1R there exists a prime
P ∈ R such that Q = S−1P . Moreover as the extension is order preserving,
I ≤P if and only if S−1I ≤S−1P . Thus we have
S−1√
I =S−1 ⋂
I≤P
P =
⋂
I≤P
S−1P =
⋂
S−1I≤S−1P
S−1P =
√
S−1I.
□
31 Localization The ring R = R[x,y ] is localized at the multiplicativeHint: Notice the complement
of S is the prime ideal of all
graphs that pass through the
origin.
set S = {f (x,y ) ∈ R | f (0, 0) ⁄= 0 }. Find all maximal ideals of S−1R and its
Jacobson radical.
Example: Localized rings are local so we are searching for a unique max-
imal ideal. The complement of S is the set P of all polynomials g(x,y ) ∈
R[x,y ] whose graph passes through the origin. Given any two polynomials
g(x,y ),h (x,y ) ∈ R[x,y ] for which g(x,y )h(x,y ) ∈P it follows g(0, 0)h(0, 0) = 0
so either g or h is in P . Clearly P is closed to sums and products and absorbs
products so P is a prime ideal. Therefore we are localizing at P . So the maximal
ideal is PP =P , and the Jacobson radical is PP as well [in commutative rings
the Jacobson radical is the intersection of maximal ideals.] □
32 Localization of Domains Let R be an integral domain with a quotientHint: Show that any element
outsideR in the intersection is
equal to a fraction of elements
that must be in R.
ﬁeld F . Prove that for any maximal ideal M of R, RM can be canonically
embedded into F and⋂
MRM =R.
Proof: The embedding follows form the universal property. Take any proper
multiplicative setS inR. Starting with the inclusion map of R intoF we notice
ι(r) is invertible in F so long as r ⁄= 0. Hence all elements s ∈ S have the
property ι(s) is invertible in F . So by the universal property of either F or
S−1R we see ι extends to a ring homomorphism ˆι : S−1R → F . Furthermore,
if ˆι(r/s) = 0 then ι(r) = 0 so r = 0 proving we have a canonical embedding.
Now consider the intersection R′ =⋂
MRM where M is a maximal ideal of
R. As R ≤ RM for each M we see R ≤ R′. Take any x ∈ R′. If x /∈ R then
deﬁne I = {y ∈R | yx ∈R}. As 0 ∈I, I is non-empty. Also r ∈R, y ∈I gives
us ryx ∈ R so ry ∈ I. The closure of sums is also clear so I is an ideal of R
and so it is contained in some maximal ideal M as clearly 1 /∈ I. Notice that
x ∈ RM as it is in the intersection of all such localizations. This means there
exist a w /∈M and r ∈R such that x =r/w. Yet this implies wx =r ∈R and
so w ∈I which it cannot be as I ≤M . The contradiction implies x ∈R in the
ﬁrst place. □

Algebra – James Wilson 137
33 Localized Modules LetR be a commutative ring and V be an R-module. Hint: Use the maximal ideal
containing the annihilator of
V .
Show that V = 0 if and only if VM = 0 for every maximal ideal M of R.
Proof: Suppose that V = 0 then clearly VM = 0.
Now suppose that VM = 0 for every localization RM at a maximal ideal M .
IfV = 0 we are done. So assume it is non-trivial so that we know its annihilator
is a proper ideal of R. Thus there exists a maximal ideal M inR containing the
annihilator of V . We localize R atM and consider VM we notice that V ≤VM
as v/1 ⁄= 0 unless v = 0. Yet VM = 0 so V = 0. □
34 Integral Fields Let A be a domain which is integral over R. Prove that Hint: Recall the result of
Exercise-5.28: integral units
are contained in the ring.
A is a ﬁeld if and only if R is as well.
Proof: Suppose A is a ﬁeld. Using Exercise- 5.28 we know if any element of R
is a unit in A then it is also a unit R, so therefore all non-zero elements in R
are invertible because they are in A.
Now suppose R is a ﬁeld. Then we use Lemma-5.3.21 to conclude A is a
ﬁeld. □
35 Integral Closure – True or False? The ring Q[x,y ] is integrally closed. Hint: Show it is a UFD.
Proof: True. Notice that Q is a PID so it is a UFD and as polynomial rings
over UFDs are UFDs we may conclude Q[x,y ] is a UFD. Now we conclude by
recalling all UFDs are integrally closed. □
36 Integral Closure – True or False? The ring Q(x)[y] is integrally closed. Hint: Show it is a UFD.
Proof: True. Notice Q(x) is a ﬁeld so it is PID and thus a UFD – although
trivially so. Hence Q(x)[y] is a UFD so as all UFDs are integrally closed we
conclude that Q(x)[y] is integrally closed. □
37 Integral Closure – True or False? The ring Z[x] is integrally closed. Hint: Show it is a UFD.
Proof: True. Notice that Z is a PID so it is a UFD and as polynomial rings
over UFDs are UFDs we may conclude Z[x] is a UFD. Now we conclude by
recalling all UFDs are integrally closed. □
38 Integral Closure LetR be a commutative integral domain. Prove that if Hint: Recall that R is the in-
tersection of the localization
at maximal ideals – Exercise-
5.32.
Rp is integrally closed for every prime ideal p ofR, then R is integrally closed.
Proof: Let a ∈ R. As such there exists a monic polynomial f (x) ∈ R[x] for
whichf (a) = 0. Now recall that R is a domain so in Rp we have R canonically
embedded as r
1 = r′
1 if and only if ur =ur′ for some u /∈ p. But being a domain
this is equivalent to r = r′. As such, f (x) ∈ R[x] ⊆ Rp[x] so we see indeed
a ∈Rp for all p so it is in the intersection of all these.
Now that we see the integral closure of the the local rings contains the
integral closure of R we may use our assumption that Rp = Rp to continue.
Recall that R is embedded in each Rp and that every maximal ideal M is
prime; thus
R ⊆
⋂
p
Rp ⊆
⋂
M
RM =R.
Hence
a ∈
⋂
p
Rp =R,
illustrating R ⊆R so naturally R =R. □

138 CHAPTER 5. RINGS
39 Idempotent Ideals Let R be a commutative noetherian local ring withHint: Use Krull’s intersection
theorem. maximal ideal M which satisﬁes M 2 =M . Prove that R is a ﬁeld.
Proof: From Krull’s intersection theorem we know J =⋂
n>0Mn =M and as
R is local J = 0; hence, M = 0 and this was a maximal ideal so indeed R is a
ﬁeld as R/M ∼=R and R/M is a ﬁeld. □
40 Finite Local Rings – True or False? Every ﬁnite local ring is a ﬁeld.Hint: Consider Z/4.
Example: False, and we may as well use the smallest example Z/4. The subring
{0, 2} is an ideal as discovered empirically [1 {0, 2} = {0, 2}, 3 {0, 2} = {0, 2}.]
Moreover the other non-zero elements are units so they cannot be adjoined to a
proper ideal; hence, Z/4 is a local ring. However 2 · 2 ≡ 0 (mod 4) so it is not
a ﬁeld. □
41 Local Artinian Rings – True or False? A local artinian ring has ﬁnitelyHint: The only prime ideal in
such a ring is the unique max-
imal ideal.
many prime ideals.
Example: True. In fact we will prove that the only prime ideal in such a ring
is the lone maximal ideal. Begin by letting J be the maximal ideal which we
notice is also the Jacobson radical as the ring is local. Now any prime ideal
P must be contained in J by the maximality. However, notice that our ring
is artinian so there exists some n such that Jn = 0 – the Jacobson radical is
nilpotent. As such, suppose, J ⁄=P so that we may take an element x ∈J −P .
This element is non-trivial in the quotient R/P . Moreover, xn = 0 as x ∈J, so
(x +P ) = xn +P = 0 + P =P so there is a nilpotent element in the quotient.
ThereforeP is not prime. Hence the only prime ideal in a local artinian ring is
the maximal ideal itself. □
42 Primary Decomposition Let R = R[x,y ], andHint: It is primary.
I =
{
f (x,y ) ∈R :f (0, 0) = ∂f
∂x (0, 0) = ∂f
∂y (0, 0)
}
.
Check that I is an ideal of R and determine if it is maximal, prime, primary, or
determine is primary decomposition.
Example: Let f ∈I and g ∈R. Consider the product gf (R is commutative
so this is suﬃcient)
gf (0, 0) = g(0, 0)f (0, 0) = g(0, 0)0 = 0;
∂
∂xfg (0, 0) = g(0, 0)∂f
∂x (0, 0) + ∂g
∂x (0, 0)f (0, 0) = 0;
∂
∂yfg (0, 0) = g(0, 0)∂f
∂y (0, 0) + ∂g
∂y (0, 0)f (0, 0) = 0.
HenceI absorbs product. Notice f (x,y ) = 0 is an element in I soI is non-empty.
Also given f,g ∈I we have
(f +g)(0, 0) = f (0, 0) +g(0, 0) = 0;
∂
∂x (f +g)(0, 0) = ∂f
∂x (0, 0) + ∂g
∂x (0, 0) = 0;
∂
∂y (f +g)(0, 0) = ∂f
∂y (0, 0) + ∂g
∂y (0, 0) = 0.
Thusf +g ∈I. Therefore I is an ideal of R.

Algebra – James Wilson 139
Noticex2 ∈I butx /∈I proving thatI is not prime, and so also not maximal.
In particular notice
I = (xiyj : i +j ≥ 2,i,j ≥ 0).
Hence √
I = (x,y )
asx2 andy2 are in I and the xiyj terms are all contained in ( x,y ). Notice
√
I is
therefore prime so I is
√
I-primary and so we have its primary decomposition. □
43 Algebraic Extensions Let M be a maximal ideal of Q[x,y,z ]. Prove Hint: Only the ﬁniteness is in
question.that F = Q[x,y,z ]/M is a ﬁnite algebraic extension of Q.
Proof: It is clear that a quotient of R = Q[x,y,z ] does not introduce any
transcendental elements, so indeed F is an algebraic extension of Q. What
must be determined is why the degree of the extension is ﬁnite.
Consider localizing R at M . It still follows that RM/MM ∼= F . However
now we recall that R is a noetherian ring so M is generated by ﬁnitely many
irreducibles. PENDING: ﬁgure out. □
44 Integrality of Polynomials Let R be a domain. Then R is integrally Hint:
closed if and only if R[x] is integrally closed.
Proof: Suppose R = R. It is clear that R[x] is a domain since R is and as
such R[x] is integrally closed if it is so inside Fr (R[x]) = Fr (R)(x). Suppose
we take a reduced fraction f (x)/g(x) ∈R[x]. This means there exists a monic
polynomial h(x,y ) ∈R[x][y] for which h(x,f (x)/g(x)) = 0. Since h is monic it
follows the leading coeﬃcient is 1 and supposing the degree is n we see:
h(x,f (x)/g(x)) = f (x)n
g(x)n +
n−1∑
i=0
ri(x)f (x)i
g(x)i = 0;
f (x)n
g(x)n = −
n−1∑
i=0
ri(x)f (x)i
g(x)i ;
f (x)n = −
n−1∑
i=0
ri(x)f (x)ig(x)n−i =g(x)
(
−
n−1∑
i=0
ri(x)f (x)ig(x)n−i−1
)
.
Hence g(x)|f (x) and as this is reduced we have g(x) = 1. As such f (x) ∈
Fr (R)[x]. We must show that indeed f (x) ∈ R[x]. PENDING: slay this
dragon! It is suﬃcient to show R[x] ≤R[x]. How is not yet known.
For the reverse direction we play set theory: Let R[x] = R[x]; thus R ⊆R ⊆
R[x] = R[x] so
R =R ∩Fr (R) ⊆R ∩Fr (R) = R ⊆R[x] ∩Fr (R) = R[x] ∩Fr (R) = R.
Hence R =R. □
45 Integral Closures and Polynomials LetR ⊆A be rings withR integrally Hint: Consider the proof that
an irreducible integer polyno-
mial is irreducible over the ra-
tionals.
closed in A. Suppose that h(x) is a polynomial in R[x] which factors in A[x]
as the product of two monic polynomials h(x) = f (x)g(x). Show that f (x) and
g(x) are each in R[x].
Proof: PENDING: yeah right. □

140 CHAPTER 5. RINGS
46 Integrality Let α ∈ C be algebraic over Q. Show α is integral over Z if Hint: Recall polynomials over
Z are irreducible in Z when-
ever they are irreducible in Q.
and only if irr(α; Q) ∈ Z[x].
Proof: If irr(α; Q) ∈ Z[x] then by deﬁnition irr(α; Q) is monic and also
irr(α; Q)(α) = 0 so indeed α is integral over Z.
Now suppose instead that α is integral over Z. Then there must exist a
monic polynomial f (x) ∈ Z[x] such that f (α) = 0. Without loss of generality
we may take f (x) to be of the lowest possible degree with α as a root. Conse-
quently,f is irreducible over Z, so by Lemma-2.2.1 we know it to be irreducible
over Q[x] as well and thus f (x) = irr(α; Q). □
47 Integral Closure over Z For each n ∈ Z ﬁnd the integral closure ofHint: Follow the steps di-
rectly. Z[√n] as follows:
(i) Reduce to the case where n is square-free.
(ii) Use the fact that √n is integral to deduce that what we want is the integral
closure R of Z in the ﬁeld Q(√n).
(iii) If α = a +b√n with a,b ∈ Q, deduce that the minimal polynomial of α
is x2 −Tr (α)x +N (α), where Tr (α) = 2α and N (α) = a2 −b2n. Thus,
using Exercise- 5.46, α ∈R if and only if 2 α and a2 −b2n are integers.
(iv) Show that if α ∈R then a ∈ 1
2 Z. If a = 0 show that α ∈R if and only if
b ∈ Z. If a = 1
2 andα ∈R, show that b ∈ 1
2 Z; thus, subtracting a multiple
of √n, we may assume b = 0 or b = 1
2 ; b = 0 is impossible.
(v) Conclude that the integral closure is Z[√n] if n ≡/ 1 (mod 4), and Z[ 1
2 +
1
2
√n] otherwise.
Proof:
(i) If n = a2m then Z[√n] = Z[√m] so without loss of generality we may
assume n is square-free.
(ii) Notice that for any n, x2 −n ∈ Z[x] so √n is integral over Z[√n]. So
the integral closure can be agreed upon to lie within Q(√n) – the ﬁeld of
fractions of Z[√n].
(iii) Given any α =a +b√n ∈ Q(√n) which is integral over Z[√n] it follows
(a +b√n)2 =a2 + 2ab√n +b2n
so we eliminate all the terms with the monic polynomial:
pα(x) = x2 − 2ax +a2 −b2n =x2 −Tr (α)x +N (α).
If the polynomial has smaller degree then α ∈ Z[√n] to begin with. There-
fore for any integral elements outside of Z[√n] we consider this to be pre-
cisely the minimal monic polynomial annihilating α. From Exercise- 5.46
we know α is integral over Z[√n] if and only if irr(α; Q(√n) ∈ Z[√n][x].
(iv) So we set about verifying when the coeﬃcients are in Z[√n]. The term
2a ∈ Z if and only if a ∈ 1
2 Z. Also when a = 0 we see b2n ∈ Z so as b ∈ Q
it follows b ∈ Z is required.
Suppose now a = 1
2 , then we require 1
4 −b2n ∈ Z so in fact 1
2 divides b.
Also, if 4 |n − 1 then
1
4 − 1
4n ∈ Z.
So if b = 1
2 then n ≡ 1 (mod 4).

Algebra – James Wilson 141
(v) So when n ≡ 1 (mod 4) we may let b = 1
2 and as such also let a = 1
2 so
we must adjoin this element to attain the closure:
Z[√n] = Z[ 1
2 + 1
2
√n].
However when n ≡/ 1 (mod 4) then a ⁄= 1/2 and consequently b ⁄= 1/2. So
indeed: Z[√n] = Z[√n].
□
48 Integral Closure of Non-UFDs Let R = Z[
√
10]. Then R is integrally Hint: Use the norm function.
closed but R is not a UFD.
Example: We have seen before that the norm N (a +b
√
10) = a2 − 10b2 has
the property that N (xy) = N (x)N (y). Thus we notice as N (2) = 4 then if
2 = ab then 4 = N (ab) = N (a)N (b). So either one of a or b is a unit, or
N (a) = N (b) = ±2. However this requires 2 = a2
1 − 10a2
2. If we pass to Z/5
any solution in Z must also produce a solution in Z/5. Yet by empirical testing
2 ≡/ a2
1 (mod 5) for any a1. Therefore there is no solution for this in Z either.
Hence 2 is irreducible in R. The same procedure shows 3, 4 +
√
10, and 4 −
√
10
are also irreducible in R. However visibly
2 · 3 = 6 = (4 +
√
10)(4 −
√
10).
Hence R is not a unique factorization domain.
Now we must demonstrate that R is yet integrally closed. Given that 10 ≡/ 1
(mod 4) we know from Exercise- 5.47 that Z[
√
10] is integrally closed. □
49 Prime Ideals of Integral Extensions Hint: Notice the extension is
an integral extension and that
any ideal lying over pZ con-
tains pR.
(i) Find all prime ideals of Z[
√
5] which lie over the prime ideal (5) of Z.
(ii) Find all prime ideals of Z[
√
5] which lie over the prime ideal (3) of Z.
(iii) Find all prime ideals of Z[
√
5] which lie over the prime ideal (2) of Z.
Example: Notice that Z[
√
5]/Z is an integral ring extension as x2 −5 is a monic
polynomial annihilating
√
5. Therefore for each prime ideal P of Z there exists
prime ideals P ′ of Z[
√
5] such that P ′ ∩ Z =P – this by the going up theorem.
Moreover by the maximality theorem we know all such P ′ are maximal in Z[
√
5]
and moreover each is incomparable – as each prime ideal of Z is maximal.
Now it is clear that if pZ ⊆P ′ whereP ′ is a prime of Z[
√
5] laying over pZ,
then pZ[
√
5] ⊆P ′.
Now suppose we consider R = Z[
√
5] and study R/pR for any prime p ∈ Z.
Clearly this yields the relation
a +b
√
5 ≡ 0 (mod pR) ⇔ p|a and p|b.
Thus we have a suitably nice Z/pZ-algebra R/pR with center all a + 0
√
5. As
any ideal of R/pR must also be a Z/pZ vector space it follows (
√
5)/pR is the
only option. Therefore this is both the Jacobson radical and the nil-radical.
More importantly, it proves that pR is (
√
5)-primary. Thus √pR is the smallest
prime ideal in R containingpR, and consequently pZ. As √pR is also maximal
(see the above argument) it is the unique prime ideal of R laying over pZ. Now
we switch to speciﬁc examples.

142 CHAPTER 5. RINGS
(i) As R5Z = 5R it follows every ideal over 5 Z contains 5R. Now the radical√
5R =
√
5R. Since
√
5R is maximal – its quotient is Z/5Z – it is prime.
Moreover, as it is a maximal prime, which by deﬁnition of begin a radical
ideal, contains all primes that contain 5 R, it is the unique prime ideal over
5Z.
(ii) Forp = 3 consider R/3R.
R/3R = {0, 1, 2,
√
5, 2
√
5, 1 +
√
5, 1 + 2
√
5, 2 +
√
5, 2 + 2
√
5}.
By testing we see for all n ⁄= 0:
1 ≡n4 ≡ (n
√
5)4 ≡ (n(1 +
√
5))8 ≡ (n(1 + 2
√
5))8 (mod 3R).
Therefore R/3R is the ﬁeld F9. Hence 3 R is maximal and so prime and
also by the fact that R(3Z) = 3R and the maximality theorem, it is the
unique prime ideal lying over 3 Z.
(iii) Forp = 2 the procedure is the same. Consider R/2R. Here we get the
elements 0, 1,
√
5, and 1 +
√
5. Notice that the only nilpotent elements
are 0 and 1 +
√
5 so they form the nil-radical.
R/2R
(1 +
√
5)/2R
0
As the quotient has all zero-divisors as nilpotent elements it follows 2 R is
(1 +
√
5)R-primary. As the radical of a primary ideal is the smallest prime
ideal containing the ideal, and this radical is also maximal, it follows it is
the unique prime ideal in R lying over 2 Z.
□
50 Prime Unions Let P1,...,P r be prime ideals of a commutative ring.Hint: ShowI times the prod-
uct of all but one prime lies in
this left out prime ideal.
Show that an ideal I which is contained in P1 ∪ · · · ∪Pr is contained in some
Pi.
Proof: Suppose I is not contained completely in any Pi. So without loss of
generality assume I ∩Pi ⁄= 0 for any i – if it does we can remove this Pi from
the union. Therefore we know Pi is not contained in Pj for any i ⁄=j.
If J =I ∩⋂
i⁄=jPi is not contained in Pj for every j, then pick xj ∈J\Pj.
Notice then x1 + · · · +xr ∈ I\(P1 ∪ · · · ∪ Pr). Yet I lies in P1 ∪ · · · ∪ Pr so
indeed there exists a j for which I ∩⋂
i⁄=jPi is contained in Pj. But this means
I∏
i⁄=jPi ⊆Pj so that I ⊆Pj as Pj is prime. □
51 Primary Decomposition LetI be a an ideal of a noetherian ring R withHint: The associated primes
of an ideal in a noetherian ring
are unique.
a reduced primary decomposition I = Q1 ∩ · · · ∩ Qr. Show that every prime
ideal of R which is minimal over I is the radical of some Qi. Is the converse
true?
Proof: We know the associated primes √Qi are the unique □
52 Prime Height Let P be a prime ideal of height r in a noetherian ringHint:
R. Show that there exists an ideal I of R with r generators over which P is
minimal.

Algebra – James Wilson 143
Proof:
□
53 Krull Dimension Let P be a prime ideal of R. Show that the height of Hint: Recall there is a bijec-
tion between the prime ide-
als of the local ring and the
primes below the prime of lo-
calization.
P is the dimension of RP .
Proof: Let {Pi : i ∈I} be a be a chain of primes of maximum length below
P – we assume the length if ﬁnite as the height is assumed to exist. Then we
know that RP has unique maximal ideal PP and because each prime below PP
there is a one-to-one correspondence with primes below P in R we see that
{PiP : i ∈I} is a maximum length chain of primes below PP .
SinceRP is a local ring, any chain of primes can be augmented to begin from
PP and as such the Krull dimension of RP will be determined by the longest
descending chain of primes from PP . As we have seen this chain has the same
length as the height of P in R so the two invariants agree. □
54 Krull Dimension Let P be a non-zero prime ideal of R. Show that Hint: Notice the pre-image,
under a surjective map, of
prime ideals is prime.
dim R≥ 1 +dim R/P.
Proof: First we resolve a simple lemma: let π :R →R/P and take any prime
Q of R/P . Then π−1(Q) is prime in R. To see this notice
R/π−1(Q) ∼= R/P
π−1(Q)/P
∼= R/P
Q ,
by the second isomorphism theorem. Since Q is prime in R/P , the quotient is
an integral domain and therefore so is R/π−1(Q). Hence we may say π−1(Q) is
prime in R.
Now take a maximum length chain of descending primes in R/P – which we
assume to exist as the Krull dimension is deﬁned.
Q0 >Q 1 > · · ·>Q m.
We pull the chain back to R by the correspondence theorem and ﬁnd
π−1(Q0)>π −1(Q1)> · · ·>π −1(Qm) ≥P >0.
Therefore we have a chain in R of primes of length at least m + 1. So we must
conclude
dim R≥ 1 +dim R/P.
□
55 Minimal Primes Let F be an algebraically closed ﬁeld. Show that Hint: Consider the associated
varieties of the minimal prime
ideals.
the minimal prime ideals of F [x1,...,x n] are the principal ideals generated by
irreducible polynomials.
Proof: Given any minimal prime ideal P , we know
√
P =P so we may pass to
the variety without loss of information. As P is minimal in R =F [x1,...,x n]
and Z is an order reversing bijection of varieties and radical ideals – to follows
Z(P ) is maximal in the set of all varieties (under set inclusion.)
AsR is noetherian there are ﬁnitely many generators fo P call themf1,...,f n
and none of them trivial. Suppose further that fi ⁄= fj for some i,j . Then
Z(fi) ⁄= Z(fj) and so Z(P ) ⊆ Z(fi) ∩Z(fj). But as Z(P ) is maximal this
cannot be so we admit f1 = · · · = fn so P = (f1). Furthermore, if f1 = g ·h
then as P is prime it contains either g or h and so f1 does not generate P .
Therefore we see f1 is irreducible.

144 CHAPTER 5. RINGS
Now take any irreducible polynomial f ∈F [x1, ˙,xn] and consider (f ). Given
gh ∈ (f ) it follows f |gh so either f |g orf |h asR is a UFD. Thus ( f ) is a prime
ideal of R. Furthermore it is a minimal prime because it does not divide other
irreducibles to which it is not associate. □
56 Generators of Varieties – True or False? Let F be a ﬁeld. If S is anHint: Choose the generators
of I(Z(S)). arbitrary subset of F [x1,...,x n], then there is a ﬁnite subset T ofF [x1,...,x n]
such that Z(S) = Z(T ).
Proof: True. PENDING: determine if algebraically closed matters. As every
ﬁeld is noetherian so is F [x1,...,x n]. Furthermore, for every subset S there is
associated a radical ideal I = I(Z(S)). As every ideal in a noetherian ring is
ﬁnitely generated let T be the generators of I. Clearly then Z(S) = Z(I) =
Z(T ). □
57 Non-radical Ideals – True or False? Let F be a ﬁeld. If I is any idealHint: Use the Nullstellensatz.
of F [x1,...,x n], then I = {f ∈F [x1,...,x n] : f (a) = 0 for each a ∈Z(I)}.
Example: False. Let F = C. Then we have the Nullstellensatz which state
I(Z(I)) =
√
I. So let n = 1 and take I = (x2). Clearly then I(Z(I)) = (x) ⁄=
(x2). □
58 Ideal Lattice and Varieties – True or False? Let F be algebraicallyHint: Note that IJ ⊆I ∩J.
closed and I,J be ideals in F [x1,...,x n]. Then Z(I) ∪Z(J) = Z(IJ ).
Proof: True. An element a ∈Fn is in Z(IJ ) if and only if f (a)g(a) = 0 for all
f ∈I and g ∈J which happens precisely when either f (a) = 0 or g(a) = 0 for
each pair f ∈I,g ∈J. That is if and only if a ∈Z(I) or a ∈Z(J). Therefore
Z(I) ∪Z(J) = Z(IJ ). □
59 Radical Ideals – True or False? Let F be a ﬁeld, and I,J be ideals inHint: Recall ifP is prime con-
taining IJ then it contains I
orJ.
F [x1,...,x n]. Then
√
I ∩J =
√
IJ .
Proof: It is clear the IJ ⊆I ∩J so
√
IJ ⊆
√
I ∩J. Now consider the reverse
inclusion.
Let P be a prime lying over IJ . It follows either I ≤ P or J ≤ P as P is
prime. In either case I ∩J ≤P . So we conclude:
√
IJ =
⋂
IJ ⊆P
P =
⋂
I∩J≤P
P =
√
I ∩J.
□
60 Direct Products with Varieties LetI andJ be ideals of A = C[x,y ] andHint: Notice if
√
I +J = A
then 1n ∈I +J soI +J =A. Z(I) ∩Z(J) = ∅. Show that A/(I ∩J) ∼=A/I ×A/J.
Proof: We begin with the given:
Z(I +J) = Z(I) ∩Z(J) = ∅.
Then we apply the Nullstellensatz:
√
I +J =I(Z(I +J)) = I(∅) = A.
Now that 1 ∈
√
I +J it follows that 1 n = 1 ∈I +J for some n. However this
implies I +J = A. Therefore we have all the ingredients of a split extension:

Algebra – James Wilson 145
both I and J are ideals, their join is A so when we quotient by I ∩J then we
have our split:
I +J/(I ∩J)
/d111 /d111 /d111 /d111 /d79/d79/d79/d79
I/(I ∩J)
/d79/d79/d79/d79 J/(I ∩J)
/d111 /d111 /d111 /d111
(I ∩J)/(I ∩J)
Thus we have by the third isomorphism theorem:
A/(I ∩J) ∼=I/(I ∩J) ×J/(I ∩J) ∼=A/J ×A/I.
□
61 DCC for Varieties – True or False? LetF be algebraically closed. Any Hint: Use the noetherian
property of F [x1,...,x n].decreasing sequence of algebraic sets in Fn stabilizes.
Proof: True. Let
Z1 ≥Z2 ≥ · · ·
be a decreasing sequence of varieties. Then as F is algebraically closed we may
use the Nullstellensatz to produce an identical length chain
I(Z1) ≤I(Z2) ≤ · · ·
inF [x1,...,x n]. However here we have an ascending chain of ideals in a noethe-
rian ring so it must stabilize, say I(Zn) = I(Zm) for all n>m . Now we reapply
the Nullstellensatz to see:
Zn =Z(I(Zn)) = Z(I(Zm) = Zm
so the descending chain of varieties stabilizes in Fn. □
62 ACC for Varieties – True or False? Let F be algebraically closed. Hint: Consider the chain of
zeros {0}, {0, 1},...Any increasing chain of algebraic sets in Fn stabilizes.
Example: False. Consider the descending chain of ideals
(x) ≥ (x(x − 1)) ≥ (x(x − 1)(x − 2)) ≥ · · ·
in C[x]. Immediately we see the associated variety chain:
Z(x) = {0} ⊊Z(x(x − 1)) = {0, 1} ⊊Z(x(x − 1)(x − 2)) = {0, 1, 2} ⊊ · · ·
ascends forever never stabilizing. □
63 ACC for Varieties – True or False? Let F be algebraically closed. Hint: Consider the Krull di-
mension of of the varieties.Any increasing sequence of irreducible algebraic sets in Fn stabilizes.
Proof: True. Given any chain of irreducible varieties
Z1 ≤Z2 ≤ · · ·
it follows the associated ideals are all prime so we get
P1 =I(Z1) ≤P2(Z2) ≤ · · ·
However if we take P = ⋃
iI(Zi) we get a prime under which is a chain of
primes. Since F [x1,...,x n] is noetherian, Krull’s ﬁnite height theorem tells us

146 CHAPTER 5. RINGS
that this chain of primes can only have ﬁnite length. Therefore the chain must
stabilizes, say Pi =Pj for all j >i. Now reapply the Nullstellensatz:
Zi =Z(I(ZI )) = Z(Pi) = Z(Pj) = Z(I(Zj)) = Zj.
Therefore an ascending chain of irreducibles must stabilize. □
64 Solution Sets and Varieties – True or False? LetF be an algebraicallyHint: Consider the variety
spanned by all fi. closed ﬁeld. A system of polynomial equations
f1(x1,...,x n) = 0
...
fm(x1,...,x n) = 0
over F has no solutions in Fn if and only if 1 can be expressed as a linear
combination 1 = ∑
ipifi with polynomial coeﬃcients pi.
Proof: True Let I = (f1,...f m).
Suppose the system has no solutions, that is: Z(I) = ∅. As F is algebraically
closed we use the Nullstellensatz to say
√
I =I(Z(I)) = I(∅) = F [x1,...,x n].
As such, 1 ∈
√
I so 1n = 1 ∈ I for some n, so indeed I = F [x1,...,x n]. As
I = (f1,...,f n) it clear that 1 = ∑
igifi for appropriate gi.
Now suppose that 1 is not a linear combination of the fi’s. It follows I is a
proper ideal and so Z(I) ⁄=emptyset. But as Z(I) is the set of all solutions to
the system we see there are in fact solutions to the system now. □
65 Zariski Topology – True or False? The Zariski topology on Fm+n isHint: The basic closed sets in
C are ﬁnite subsets of C while
C2 includes the uncountably
inﬁnite lines.
the product topology of the Zariski topologies on Fn and Fm.
Example: False. The product topology has too few closed sets. For instance,
consider F = C and n = m = 1. In C the varieties are all ﬁnite subsets of C.
For C2 the varieties also include such things as the line through y −x which
when projected in R is y = x – clearly an uncountably inﬁnite set of points.
However if C2 where to have the same Zariski topology as C × C then this line
– a closed set in C2 – would have to be the ﬁnite union of basic closed sets in
C×C. The basic sets in C×C are all products of ﬁnite subsets which are clearly
always ﬁnite. Thus the task is impossible. □
66 Zariski Topology Let R be any ring. Denote by Spec R the set of theHint:
prime ideals of R. For any ideal I ⊴R denote
Z(I) := {P ∈Spec R : I ≤P }.
Introduce the Zariski topology on SpecR by declaring the sets of the form Z(I)
to be closed. Deﬁne a distinguished open set of Spec Rto a set of the form
U (f ) := {P ∈Spec R : f /∈P }
where f ∈R.
(a) Prove that this is indeed a topology.

Algebra – James Wilson 147
(b) Prove that distinguished opens sets are indeed open, and moreover, they
form a basis of the Zariski topology. Show that SpecR =⋃
iU (fi) for some
collection fi of elements of R if and only if the ideal generated by all the
fi’s is R.
(c) Prove that Spec Ris compact in the Zariski topology.
Proof: PENDING: when pigs ﬂy and quals pass. □
67 Zariski Topology and Frobenius – True or False? Let F be an Hint:
algebraically closed ﬁeld of characteristic p >0, and Fr : F → F : a ↦→ ap be
the Frobenius homomorphism. True or False:
(i) Fr is a homeomorphism in the Zariski topology.
(ii) Fr is an isomorphism of algebraic sets.
(i) Proof: True.
□
(ii) Example:
□
68 Automorphisms of Varieties Describe all automorphism of the algebraic Hint:
set F .
Example:
□
69 Isomorphism of Varieties Which of the following algebraic sets over C Hint:
are isomorphic.
(i) C;
(ii) Z(x) ⊂ C2;
(iii) Z(y −x2) ⊂ C2;
(iv) Z(y2 −x3) ⊂ C2;
(v) Z(y2 −x3 −x2) ⊂ C2.
Example:
□

148 CHAPTER 5. RINGS

Bibliography
[Hun74] Thomas W. Hungerford, Algebra, Springer-Verlag, New York, 1974.
[Kle03] Alexander Kleshchev, Lectures on abstract algebra for graduate stu-
dents, pre-print, University of Oregon, Eugene, Oregon, 2003.
[Rot02] Joseph J. Rotman, Advanced modern algebra , Prentice Hall, Upper
Saddle River, New Jersey, 2002.
149

Index
An
C15, 25
conjugacy classes, 30
embedding, 25
Sn
S4, 20
automorphisms, 23
center, 14
conjugacy classes, 30
generators, 31
transitive subgroups, 7, 20
Q, 107
p-th roots, 48
actions
on roots, 40
algebras, 94
classiﬁcation, 97
commutative, 93, 94
complex, 95, 97
cyclic group algebras, 93
dimension, 95, 97
direct products, 144
division, 91
ﬁnite dimensional, 91, 93, 94
group algebras, 92, 93
over algebraically closed ﬁelds,
92
real, 97
simple, 104
tensors, 115
zero-divisors, 91
Automorphisms
cyclic groups, 8
automorphisms, 23
of ﬁelds, 39
varieties, 147
Burnside’s Formula, 7
commutative
probability, 7
conjugation, 30
2 conjugacy classes, 19
as generators, 16
intersection, 17
of Sylow subgroups, 17
unions, 15, 16
Consider the lattice above the inter-
section., 85
Dihedral, 31
dihedral, 23
18, 28
representation, 19
domains, 39
endomorphism, 70
over tensors, 120
semi-simple modules, 105
endomorphisms, 80, 85, 86
center, 91
of noetherian modules, 83
Extensions
algebraic, 37
normal, 38
of algebraic ﬁelds, 37
simple, 37
extensions
algebraic, 39
degree, 44
domains, 39
inseparable, 49
nilpotent, 12
normal, 43, 48
separable, 48, 49
simple, 50
transcendental, 39
Fields
A, 37
algebraic extensions, 37
countable, 37
extensions of Q, 37
Galois group order, 37
normal extensions, 38
towers, 37
ﬁelds, 135
algebraic extensions, 39, 139
algebraically closed, 92, 93, 143,
144
automorphisms, 39
150

INDEX Algebra – James Wilson 151
extensions, 43
ﬁnite, 47–50
Galois extensions, 45
inﬁnite, 41
integral, 137
intermediate, 49
isomorphism, 38
monomorphisms, 44
normal extensions, 43
of Rational Functions, 48
perfect, 39
projective, 108, 113
splitting, 49
splitting ﬁelds, 41
squares, 50
tensors, 123
transcendental, 44
Frattini, 8
free
groups, 29
Frobenius
homomorphism, 48
Frobenius homomorphism, 147
group algebra
zero-divisors, 86
Groups
conjugacy classes, 24
cyclic, 7
Galois, 37
inﬁnite, 8
Pr¨ ufer,7
groups
An, 22
F ×, 41
HK -complex, 13
Sn, 22
Q, 15
p-groups, 28
“local” groups, 10
abelian groups, 80–83
action, 17, 22
alternating, see An
automorphisms, 27
counter examples, 26
diagonal embedding, 28
ﬁnite, 86
ﬁnite abelian groups, 81
free, 29
free-abelian, 29
Frobenius groups, 22
Galois, 45
Galois group, 40
Galois groups, 41
generators, 16
Hamiltonian, 14
invariant factors, 82
involutions, 11
metabelian, 20
nilpotent, 10–12, 20
of involutions, 27
of matrices, 16
of symmetries, 30
order p(p + 1), 22
order pq, 20
order pqr, 21
order 175, 28
parallelogram law, 13
products, 26
simple, 18, 21, 22, 28
solvable, 27
transitive, 20
trivial, 19
Hamiltonian, 14
Hilbert Basis Theorem, 132, 133
Hilbert’s Nullstellensatz, 144, 146
Hom, 75
ideals
associated primes, 130
idempotent, 138
irreducible, 129
Jacobson Radical, 136
laying over, 141
localization, 136
maximal, 132, 133, 135, 136,
138
nil-radical, 132
primary, 129, 130, 132, 135, 138
primary decomposition, 130, 138,
142
prime, 129–135, 137, 138, 141–
144
prime height, 142, 143
products, 144
radical, 130, 136, 144
radicals, 130
idempotents, 87, 88, 97
irreducible
polynomial, 37
irreducibles, 135
Jacobson Density Theorem, 93
Jacobson Radical, 87, see rngs88
Maschke’s Theorem
counter example, 71
matrices

152 INDEX
GLn(Fq), 16
characteristic polynomial, 99, 101,
103, 104
companion matrix, 98, 99
elementary divisors, see ivari-
ant factors76, 98, 99, 104
equivalent, 79
invariant factors, 76, 78, 98, 99,
103
Jacobson Radical, 89
Jordan Normal Form, 104
linear transforms, 103
minimal polynomial, 98, 99, 101,
103, 104
minimal polynomials, 99
nilpotent, 99
nullity, 101
Rational Canonical Form, 72,
98, 99
relations, 103
similarity, 98, 99
similarity classes, 99, 101
simple artinian rings, 92
Smith Normal Form, 72, 76, 78
subrings, 85
uni-triangular, 19
unimodular, 78, 79
matrix
diagonalization, 100, 101
modules
RR, 79
A.C.C., 69
ACC, 86
annihilator, 71
annihilators, 90
ascending chain condition, see
A.C.C.
basis, 70
classiﬁcation, 82
composition series, 73
cyclic, 84, 108
D.C.C., 69
decomposition, 71, 103
descending chain condition, see
D.C.C.
diagonal embeddings, 71
diagonal submodules, 83
direct sums, 83–85
divisible, 106
divisor chains, 72
dual, 112, 113
dual basis, 112
dual vector spaces, 113
elementary divisors, see ivari-
ant factors76
endomorphism ring, 70
endomorphisms, 80
ﬂat, 117, 118
free, 70, 72–74, 80, 81, 106, 107,
112, 122
free modules, 73, 74
free quotients, 81
free submodules, 73
generators, 79, 90
indecomposable, 85, 105
induced, 119
induced modules, 121
injective, 106–111
injective hull, 111
invariant factors, 76, 78–80, 82,
83, 99
Jacobson Radical, 104
left regular module, 79
left vs. right, 68
linear transformations, 101
localization, 137
noetherian, 83
of matrices, 85
of quotient rings, 119
over algebras, 94
over artinian rings, 69
over commutative rings, 81
over division rings, 113
over domains, 113
over ﬁelds, 113
over ﬁnite rings, 73
over noetherian rings, 86
over PID’s, 72
over PIDs, 73, 74, 76, 79, 80,
82, 83, 107, 110, 114
primary decomposition, 80, 83
projective, 106–108, 110, 112,
113
pure submodules, 76
quotients, 69, 71, 81, 85, 108,
110
rank, 79, 81
semi-simple, 87, 105, 111, 112
short exact sequences, 105
simple, 83, 84, 86, 91, 93, 94
submodule complements, 71
submodules, 69, 76, 108
sums, 69
tensors, 114
torsion, 115
torsion free, 74, 80
vector spaces, 101, 113

INDEX Algebra – James Wilson 153
multiplicative sets, 131
Nakayama’s Lemma, 90
Nilpotent, 23
nilpotent, 23, 87, 88, 91, 97, 132
center, 26
extensions, 12
groups of order 18, 28
normalizer, 21
Parallelogram Law, 13, 15
permutation groups
C15, 25
polynomial
degree, 44
polynomials, 132
characteristic, see mtrices99
counting, 49
extensions, 43
irreducible, 129
minimal, see mtrices99
over ﬁelds, 47
primes
height, 145
Products
groups, 28
Pr¨ ufer group,109
relations
dihedral, 19
trivial, 19
rings
Homr, 75
Z/m, 88
Z/nZ, 109
annihilator, 71
artinian, 68, 73, 74, 91, 97, 104,
106, 112, 133, 138, 145
classiﬁcation, 88
commutative, 71, 106
composition series, 73
decomposition, 79, 132
direct sums, 90
division rings, 86, 91, 95–97, 104,
113
domains, 73, 136
endomorphism ring, 85
ﬁnite, 95, 138
ﬁnite rings, 95
formal power series, 72, 129
fraction ﬁeld, 110, 115
injective hull, 111
integral closure, 140, 141
integral elements, 135
integral extensions, 137, 139–
141
integrally closed, 137, 139
J(R), see Jcobson Radical88
Jacobson Radical, 88–90, 96, 129
Krull dimension, 143
local, 131, 132, 138, 143
local rings, 96
localization, 130, 131, 136, 137
localization at primes, 131
maximal ideals, 105
nil-radical, 87
noetherian, 68, 73, 86, 106, 130,
132, 133, 142–146
non-commutative, 71
non-UFDs, 141
of endomorphisms, 70
of idempotents, 97
of polynomials, 74, 132, 133
PID, 72–74
PIDs, 88, 90, 99, 132, 133
polynomials, 139
primary decomposition, 142
primary ideals, see ieals129
prime localization, 137
Principal Ideal Domains, see PID
quotients, 74, 133
semi-simple, 87, 88, 91, 97
semi-simple artinian, see smi-
simple87, 96, 105, 111, 112
simple, 95
simple artinian, 92
subrings, 74, 133
tensors, 123
UFDs, 130, 132, 133, 141
Unique Factorization Domains,
see UDs130
units, 135
zero-divisors, 91
Schur’s Lemma, 91, 93
semi-simple
commutative, 87
simple
Sylow-2-subgroups, 18
Sylow-subgroups, 28
subgroup
Frattini, 8
second isomorphism, 12
subgroups
Cp ×Cp, 27
p-chains, 9
p-subgroup chains, 11
p-subgroups, 25

154 INDEX
center, 14, 23, 25, 26, 28
centralizer, 30
complex, 13
conjugations, 15, 16
counter examples, 26
cyclic Sylow-2-subgroup, 22
cyclic Sylow-subgroups, 11
index, 15
index 2, 22
inﬁnite, 8
inherited subgroups, 21
intersections, 15
join, 13
maximal subgroups, 10
minimal p-quotient subgroups,
9
normal, 13, 22, 24
normal chains, 9
normal subgroups, 10
normal transitivity, 12
normalizer, 21, 25
normalizer of Sylow subgroup,
21
normalizers, 23
of Q, 15
of orders dividing, 10
parallelogram law, 12
quotients, 24
Sylowp-subgroups, 9
Sylow subgroups, 17
Sylow-subgroups, 28
Sylow
normalizer, 21
Sylow subgroups, 21
Sylow-subgroups
normality, 25
of normal subgroups, 24
of quotients, 24
symmetries, 30
tensors, 123, 135
annihilators, 121, 122
dimension, 121, 123
examples, 122
ﬂat, 122
identity tensor, 122
induced modules, 121
isomorphism, 116
killing torsion, 115, 121, 122
of algebras, 115
of endomorphisms, 120
of exact sequences, 117, 118
of ﬂat modules, 118
of fraction ﬁelds, 115
of free modules, 121
of maps, 120
of quotients, 116, 119
of split exact sequences, 117
of subrings, 114
over Z, 116
over division rings, 121
over ﬁelds, 123
over free modules, 122
over PIDs, 114
quotients, 122
transcendental
extensions, 39
Galois group, 41
transitive
embedding, 7
True/False
C15 as a Permutation Group.,
25
S4, 20
pk-th roots in Finite Fields., 48
pq-groups, 20
ACC for Varieties, 145
Algebraic Towers., 37
Annihilating Modules, 121
Applied Tensors, 122
Artinian Rings, 132
Centrality in p-groups., 28
Commutative Algebras, 93, 94
Commutative Semi-simple Rings,
87
Complex Algebra Dimensions,
95
Complex dimension 3 Algebras,
97
Complex dimension 4 Algebras,
97
Composition Series, 73
Counter Examples., 26
Counting Involutions, 11
Cyclic Automorphisms, 8
Cyclic Groups, 7
DCC for Varieties, 145
Dihedral Groups., 31
Dihedral Nilpotency., 23
Dimension and Tensors, 121
Division Algebras, 91
Division Rings, 91, 96
Domain Extensions., 39
Endomorphisms over PIDs, 80
Field Isomorphisms., 38
Field Monomorphisms., 44
Fields and Tensors, 123
Finite Local Rings, 138

INDEX Algebra – James Wilson 155
Fraction Field Tensors, 115
Free Inheritance, 74
Free PID Modules, 73
Free Quotients, 81
Free Submodules, 73
Galois Group Order., 37
Generators of Varieties, 144
Hamiltonian Groups, 14
Ideal Lattice and Varieties, 144
Identity Tensor, 122
Indecomposable Modules, 105
Injective Z-modules, 109
Injective Hulls, 111
Injective Modules, 106
Integral Closure, 137
Invariant Factors, 79
Jacobson Radical, 88, 90, 129
Left Regular Modules, 79
Local Artinian Rings, 138
Localization and Radicals, 136
Localization of Ideals, 136
Localized Local Rings, 131
Matrix Equivalence, 79
Matrix Subrings, 85
Module Annihilators., 71
Module Quotients, 85
Nilpotency in Semi-simple Rings,
87
Nilpotency of order 18., 28
Nilpotent Free Rings, 97
Nilpotent Ideal, 87
Nilpotent Subgroups, 10
Noetherian Modules, 83, 86
Noetherian PIDs, 133
Noetherian Rings, 132, 133
Non-radical Ideals, 144
Normal Extensions of C., 48
Normal Extensions., 48
Normal Sylow-subgroups., 25
Normal Transitivity, 12
Normal Transitivity., 38
Normalizers of Sylow subgroups,
21
PID Quotients, 74
PID subrings, 74
Polynomial Rings, 106, 132
Polynomials over Artinian Rings,
74
Polynomials over PIDs, 74
Primary Ideals, 132
Prime Ideals, 133, 135
Prime Intersection, 134
Projective R[x]-modules, 112
Projectives over PIDs, 110
Projectivity and Freeness, 112
Quotients and Tensors, 122
Radical Ideals, 144
Rank Ordering, 81
Schur’s Lemma, 91
Schur’s Lemma Converse, 86
Semi-simple Modules, 111
Semi-simple Rings, 88
Similarity Classes, 99
Simple Artinian Rings, 92
Simple Extensions., 37
Solution Sets and Varieties, 146
Tensor Isomorphisms, 116
Tensored Maps, 120
Tensors, 135
Tensors over Free Modules, 122
Torsion and Tensors, 115
Torsion Free vs. Free, 74, 80
Transcendental Galois Groups.,
41
Transitive Subgroups of S5, 20
UFDs, 133
Uniqueness of Module Decom-
position., 71
Zariski Topology, 146
Zariski Topology and Frobenius,
147
Zero-Divisors in Group Algebras,
86
v. Dyck, 19
varieties, 139, 144
ACC, 145
ascending chain condition, see
AC145
automorphisms, 147
DCC, 145
descending chain condition, see
DC145
generators, 144
isomorphism, 147
lattice, 144
singular points, 143
solution sets, 146
trivial intersections, 144
Zariski Topology, 146
Wedderburn-Artin, 91, 95
Zariski Topology, 146
over characteristic p, 147

