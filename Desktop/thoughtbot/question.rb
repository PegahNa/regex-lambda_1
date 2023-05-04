# frozen_string_literal: true

require_relative './thoughtbot/question'
class Person
  def initialize(first_name:, last_name:, middle_name: nil)
    @first_name = first_name
    @middle_name = middle_name
    @last_name = last_name
  end

  def full_name
    if @middle_name.nil? || @middle_name.empty?
      "#{@first_name} #{@last_name}"
    else
      "#{@first_name[0]} #{@middle_name[0]} #{@last_name[0]}"
    end
  end

  def full_name_with_middle_initial
    if @middle_name.nil? || @middle_name.empty?
      "#{@first_name[0]} #{@last_name[0]}"
    else
      "#{@first_name[0]} #{@middle_name[0]} #{@last_name[0]}"
    end
  end

  def initials
    middle_initial = @middle_name.nil? || @middle_name.empty? ? '' : @middle_name[0]
    "#{@first_name[0]}#{middle_initial}#{@last_name[0]}"
  end
end
