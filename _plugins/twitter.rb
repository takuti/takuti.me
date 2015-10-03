
require 'open-uri'
require 'json'

# convert tweet url to emmbededding html
def url2emb(content)
  converted_content = content
  content.scan(/(https?:\/\/twitter\.com\/[a-zA-Z0-9_]+\/status\/([0-9]+)\/?)/).each { |url, id|
    json = open("https://api.twitter.com/1/statuses/oembed.json?id=#{id}").read
    html = JSON.parse(json)['html']
    converted_content = converted_content.gsub(/#{url}/, html)
  }
  converted_content
end


module Jekyll

  # for markdown, extend oroginal parser's convert function
  module Converters
    class Markdown
      class KramdownParser
        alias :original_convert :convert
        def convert(content)
          content = url2emb(content)
          original_convert(content)
        end
      end
    end
  end

  # for html, extend converter as a plugin
  class TweetUrl2Emb < Converter
    safe true
    priority :low

    def matches(ext)
      ext =~ /^\.html$/i
    end

    def output_ext(ext)
      '.html'
    end

    def convert(content)
      url2emb(content)
    end
  end

end
