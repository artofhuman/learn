def longest_common_prefix1(strs)
  s1 = strs.min
  s2 = strs.max

  s1.chars.each_with_index do |ch, i|
    if ch != s2[i]
      return s1[0, i]
    end
  end

  s1
end


puts longest_common_prefix1(["flower","flow","flight"])
