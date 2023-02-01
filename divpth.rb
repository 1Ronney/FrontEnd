#!/usr/bin/env ruby
puts ARGV[0].scan(/div in htm def. a generic block of content/\{these contents do not carry[any semantic value]\s
  \[they are hence used for layout elements such as containers]\/).join(',')
