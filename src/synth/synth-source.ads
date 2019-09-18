--  Source/origin of synthesis.
--  Copyright (C) 2017 Tristan Gingold
--
--  This file is part of GHDL.
--
--  This program is free software; you can redistribute it and/or modify
--  it under the terms of the GNU General Public License as published by
--  the Free Software Foundation; either version 2 of the License, or
--  (at your option) any later version.
--
--  This program is distributed in the hope that it will be useful,
--  but WITHOUT ANY WARRANTY; without even the implied warranty of
--  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
--  GNU General Public License for more details.
--
--  You should have received a copy of the GNU General Public License
--  along with this program; if not, write to the Free Software
--  Foundation, Inc., 51 Franklin Street - Fifth Floor, Boston,
--  MA 02110-1301, USA.

with Netlists;

with Vhdl.Nodes; use Vhdl.Nodes;

package Synth.Source is
   subtype Syn_Src is Iir;
   No_Syn_Src : constant Syn_Src := Null_Iir;

   procedure Set_Location (N : Netlists.Net; Src : Syn_Src);
   pragma Inline (Set_Location);
end Synth.Source;
