CONJECTUREPANEL Proofs
PROOF "(G→B), (C→D), G, C ⊢ G∧C∧B∧D"
INFER (G→B),
     (C→D),
     G,
     C 
     ⊢ G∧C∧B∧D 
FORMULAE
0 D,
1 G∧C∧B,
2 B,
3 G∧C,
4 G∧C∧B∧D,
5 C,
6 G,
7 G→B,
8 C→D 
IS
SEQ (cut[B,C\0,4]) ("→ elim"[A,B\5,0]) (hyp[A\8]) (hyp[A\5]) (cut[B,C\2,4]) ("→ elim"[A,B\6,2]) (hyp[A\7]) (hyp[A\6]) (cut[B,C\3,4]) ("∧ intro"[A,B\6,5]) (hyp[A\6]) (hyp[A\5]) (cut[B,C\1,4]) ("∧ intro"[A,B\3,2]) (hyp[A\3]) (hyp[A\2]) ("∧ intro"[A,B\1,0]) (hyp[A\1]) (hyp[A\0])
END
CONJECTUREPANEL Proofs
PROOF "¬B→¬G, ¬B ⊢ ¬B∧¬G"
INFER ¬B→¬G,
     ¬B 
     ⊢ ¬B∧¬G 
FORMULAE
0 ¬B∧¬G,
1 ¬G,
2 ¬B,
3 ¬B→¬G 
IS
SEQ (cut[B,C\1,0]) ("→ elim"[A,B\2,1]) (hyp[A\3]) (hyp[A\2]) (cut[B,C\0,0]) ("∧ intro"[A,B\2,1]) (hyp[A\2]) (hyp[A\1]) (hyp[A\0])
END
CONJECTUREPANEL Proofs
PROOF "(¬A∨¬R)→F, Q, ¬A, ¬R ⊢ Q∧F"
INFER (¬A∨¬R)→F,
     Q,
     ¬A,
     ¬R 
     ⊢ Q∧F 
FORMULAE
0 F,
1 Q,
2 Q∧F,
3 ¬A∨¬R,
4 ¬A∨¬R→F,
5 ¬A,
6 ¬R,
7 (¬A∨¬R)→F 
IS
SEQ (cut[B,C\3,2]) (LAYOUT "∨ intro" (0) ("∨ intro(L)"[B,A\6,5]) (hyp[A\5])) (cut[B,C\0,2]) ("→ elim"[A,B\3,0]) (hyp[A\4]) (hyp[A\3]) (cut[B,C\0,2]) (hyp[A\0]) ("∧ intro"[A,B\1,0]) (hyp[A\1]) (hyp[A\0])
END
CONJECTUREPANEL Theorems
PROOF "¬¬P ⊢ P"
INFER ¬¬P 
     ⊢ P 
FORMULAE
0 ⊥,
1 ¬¬P,
2 ¬P,
3 P 
IS
SEQ ("contra (classical)"[A\3]) (cut[B,C\0,0]) ("¬ elim"[B\2]) (hyp[A\2]) (hyp[A\1]) (hyp[A\0])
END
CONJECTUREPANEL Theorems
PROOF "P→Q ⊢ ¬Q→¬P"
INFER P→Q 
     ⊢ ¬Q→¬P 
FORMULAE
0 ⊥,
1 ¬Q,
2 Q,
3 P,
4 P→Q,
5 ¬P 
IS
SEQ ("→ intro"[A,B\1,5]) ("¬ intro"[A\3]) (cut[B,C\2,0]) ("→ elim"[A,B\3,2]) (hyp[A\4]) (hyp[A\3]) (cut[B,C\0,0]) ("¬ elim"[B\2]) (hyp[A\2]) (hyp[A\1]) (hyp[A\0])
END
CONJECTUREPANEL Theorems
PROOF "P→Q, ¬Q ⊢ ¬P"
INFER P→Q,
     ¬Q 
     ⊢ ¬P 
FORMULAE
0 ⊥,
1 ¬Q,
2 Q,
3 P,
4 P→Q 
IS
SEQ ("¬ intro"[A\3]) (cut[B,C\2,0]) ("→ elim"[A,B\3,2]) (hyp[A\4]) (hyp[A\3]) (cut[B,C\0,0]) ("¬ elim"[B\2]) (hyp[A\2]) (hyp[A\1]) (hyp[A\0])
END
CONJECTUREPANEL Proofs
PROOF "R→(Q∧A), R ⊢ R∧Q∧A"
INFER R→(Q∧A),
     R 
     ⊢ R∧Q∧A 
FORMULAE
0 R∧Q∧A,
1 A,
2 R∧Q,
3 Q,
4 R,
5 Q∧A,
6 R→Q∧A,
7 R→(Q∧A)
IS
SEQ (cut[B,C\5,0]) ("→ elim"[A,B\4,5]) (hyp[A\6]) (hyp[A\4]) (cut[B,C\1,0]) (LAYOUT "∧ elim" (0) ("∧ elim(R)"[A,B\3,1]) (hyp[A\5])) (cut[B,C\3,0]) (LAYOUT "∧ elim" (0) ("∧ elim(L)"[A,B\3,1]) (hyp[A\5])) (cut[B,C\2,0]) ("∧ intro"[A,B\4,3]) (hyp[A\4]) (hyp[A\3]) (cut[B,C\0,0]) ("∧ intro"[A,B\2,1]) (hyp[A\2]) (hyp[A\1]) (hyp[A\0])
END
CONJECTUREPANEL Proofs
PROOF "T→(S∧D), T ⊢ S∧T∧D"
INFER T→(S∧D),
     T 
     ⊢ S∧T∧D 
FORMULAE
0 S∧T∧D,
1 D,
2 S∧T,
3 T,
4 S,
5 S∧D,
6 T→S∧D,
7 T→(S∧D)
IS
SEQ (cut[B,C\5,0]) ("→ elim"[A,B\3,5]) (hyp[A\6]) (hyp[A\3]) (cut[B,C\1,0]) (LAYOUT "∧ elim" (0) ("∧ elim(R)"[A,B\4,1]) (hyp[A\5])) (cut[B,C\4,0]) (LAYOUT "∧ elim" (0) ("∧ elim(L)"[A,B\4,1]) (hyp[A\5])) (cut[B,C\2,0]) ("∧ intro"[A,B\4,3]) (hyp[A\4]) (hyp[A\3]) (cut[B,C\0,0]) ("∧ intro"[A,B\2,1]) (hyp[A\2]) (hyp[A\1]) (hyp[A\0])
END
CONJECTUREPANEL Theorems
PROOF "P∨¬P"
INFER P∨¬P 
FORMULAE
0 ⊥,
1 ¬(P∨¬P),
2 P∨¬P,
3 P,
4 ¬P,
5 ¬(P∨¬P)
IS
SEQ ("contra (classical)"[A\2]) (cut[B,C\3,0]) ("contra (classical)"[A\3]) (cut[B,C\2,0]) (LAYOUT "∨ intro" (0) ("∨ intro(R)"[B,A\3,4]) (hyp[A\4])) (cut[B,C\0,0]) ("¬ elim"[B\2]) (hyp[A\2]) (hyp[A\1]) (hyp[A\0]) (cut[B,C\2,0]) (LAYOUT "∨ intro" (0) ("∨ intro(L)"[B,A\4,3]) (hyp[A\3])) (cut[B,C\0,0]) ("¬ elim"[B\2]) (hyp[A\2]) (hyp[A\1]) (hyp[A\0])
END
CONJECTUREPANEL Theorems
PROOF "P ⊢ ¬¬P"
INFER P 
     ⊢ ¬¬P 
FORMULAE
0 ⊥,
1 ¬P,
2 P 
IS
SEQ ("¬ intro"[A\1]) (cut[B,C\0,0]) ("¬ elim"[B\2]) (hyp[A\2]) (hyp[A\1]) (hyp[A\0])
END
CONJECTUREPANEL Proofs
PROOF "F→¬A, F ⊢ F∧¬A"
INFER F→¬A,
     F 
     ⊢ F∧¬A 
FORMULAE
0 F∧¬A,
1 ¬A,
2 F,
3 F→¬A 
IS
SEQ (cut[B,C\1,0]) ("→ elim"[A,B\2,1]) (hyp[A\3]) (hyp[A\2]) (cut[B,C\0,0]) ("∧ intro"[A,B\2,1]) (hyp[A\2]) (hyp[A\1]) (hyp[A\0])
END
