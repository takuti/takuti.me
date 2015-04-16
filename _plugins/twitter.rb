require 'open-uri'
require 'json'

=begin
def sub_twitter_url(content)
  content.scan(/(https?:\/\/twitter\.com\/[a-zA-Z0-9_]+\/status\/([0-9]+)\/?)/).each { |url, id|
    json = open("https://api.twitter.com/1/statuses/oembed.json?id=#{id}").read
    html = JSON.parse(json)['html']
    content = content.gsub(/#{url}/, html)
  }
  content
end

module Jekyll
  class HtmlTwitterEmb < Converter
    safe true
    priority :low

    def matches(ext)
      ext =~ /^\.html$/i
    end

    def output_ext(ext)
      ".html"
    end

    def convert(content)
      sub_twitter_url(content)
    end
  end

  module Converters
    class Markdown
      class CustomizedMarkdownParser < RedcarpetParser
        def convert(content)
          super(sub_twitter_url(content))
        end
      end
    end
  end
end
=end
