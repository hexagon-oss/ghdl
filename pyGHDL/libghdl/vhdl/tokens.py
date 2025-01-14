# Auto generated Python source file from Ada sources
# Call 'make' in 'src/vhdl' to regenerate:
#
from enum import IntEnum, unique
from pydecor import export


@export
@unique
class Tok(IntEnum):
    Invalid = 0
    Eof = 1
    Newline = 2
    Block_Comment_Start = 3
    Block_Comment_End = 4
    Block_Comment_Text = 5
    Line_Comment = 6
    Character = 7
    Identifier = 8
    Integer = 9
    Real = 10
    String = 11
    Bit_String = 12
    Integer_Letter = 13
    Left_Paren = 14
    Right_Paren = 15
    Left_Bracket = 16
    Right_Bracket = 17
    Colon = 18
    Semi_Colon = 19
    Comma = 20
    Double_Arrow = 21
    Tick = 22
    Double_Star = 23
    Assign = 24
    Bar = 25
    Box = 26
    Dot = 27
    Equal_Equal = 28
    Equal = 29
    Not_Equal = 30
    Less = 31
    Less_Equal = 32
    Greater = 33
    Greater_Equal = 34
    Match_Equal = 35
    Match_Not_Equal = 36
    Match_Less = 37
    Match_Less_Equal = 38
    Match_Greater = 39
    Match_Greater_Equal = 40
    Plus = 41
    Minus = 42
    Ampersand = 43
    Question_Mark = 44
    Condition = 45
    Double_Less = 46
    Double_Greater = 47
    Caret = 48
    And_And = 49
    Bar_Bar = 50
    Left_Curly = 51
    Right_Curly = 52
    Exclam_Mark = 53
    Brack_Star = 54
    Brack_Plus_Brack = 55
    Brack_Arrow = 56
    Brack_Equal = 57
    Bar_Arrow = 58
    Bar_Double_Arrow = 59
    Minus_Greater = 60
    Equiv_Arrow = 61
    Arobase = 62
    Star = 63
    Slash = 64
    Mod = 65
    Rem = 66
    Abs = 67
    Not = 68
    Access = 69
    After = 70
    Alias = 71
    All = 72
    Architecture = 73
    Array = 74
    Assert = 75
    Attribute = 76
    Begin = 77
    Block = 78
    Body = 79
    Buffer = 80
    Bus = 81
    Case = 82
    Component = 83
    Configuration = 84
    Constant = 85
    Disconnect = 86
    Downto = 87
    Else = 88
    Elsif = 89
    End = 90
    Entity = 91
    Exit = 92
    File = 93
    For = 94
    Function = 95
    Generate = 96
    Generic = 97
    Guarded = 98
    If = 99
    In = 100
    Inout = 101
    Is = 102
    Label = 103
    Library = 104
    Linkage = 105
    Loop = 106
    Map = 107
    New = 108
    Next = 109
    Null = 110
    Of = 111
    On = 112
    Open = 113
    Others = 114
    Out = 115
    Package = 116
    Port = 117
    Procedure = 118
    Process = 119
    Range = 120
    Record = 121
    Register = 122
    Report = 123
    Return = 124
    Select = 125
    Severity = 126
    Signal = 127
    Subtype = 128
    Then = 129
    To = 130
    Transport = 131
    Type = 132
    Units = 133
    Until = 134
    Use = 135
    Variable = 136
    Wait = 137
    When = 138
    While = 139
    With = 140
    And = 141
    Or = 142
    Xor = 143
    Nand = 144
    Nor = 145
    Xnor = 146
    Group = 147
    Impure = 148
    Inertial = 149
    Literal = 150
    Postponed = 151
    Pure = 152
    Reject = 153
    Shared = 154
    Unaffected = 155
    Sll = 156
    Sla = 157
    Sra = 158
    Srl = 159
    Rol = 160
    Ror = 161
    Protected = 162
    Assume = 163
    Context = 164
    Cover = 165
    Default = 166
    Force = 167
    Parameter = 168
    Property = 169
    Release = 170
    Restrict = 171
    Restrict_Guarantee = 172
    Sequence = 173
    Inherit = 174
    Vmode = 175
    Vprop = 176
    Vunit = 177
    Across = 178
    Break = 179
    Limit = 180
    Nature = 181
    Noise = 182
    Procedural = 183
    Quantity = 184
    Reference = 185
    Spectrum = 186
    Subnature = 187
    Terminal = 188
    Through = 189
    Tolerance = 190
    Psl_Clock = 191
    Psl_Endpoint = 192
    Psl_Const = 193
    Psl_Boolean = 194
    Inf = 195
    Within = 196
    Abort = 197
    Async_Abort = 198
    Sync_Abort = 199
    Before = 200
    Before_Em = 201
    Before_Un = 202
    Before_Em_Un = 203
    Always = 204
    Never = 205
    Eventually_Em = 206
    Next_Em = 207
    Next_A = 208
    Next_A_Em = 209
    Next_E = 210
    Next_E_Em = 211
    Next_Event = 212
    Next_Event_Em = 213
    Next_Event_A = 214
    Next_Event_A_Em = 215
    Next_Event_E = 216
    Next_Event_E_Em = 217
    Until_Em = 218
    Until_Un = 219
    Until_Em_Un = 220
    Prev = 221
    Stable = 222
    Fell = 223
    Rose = 224
    Onehot = 225
    Onehot0 = 226
