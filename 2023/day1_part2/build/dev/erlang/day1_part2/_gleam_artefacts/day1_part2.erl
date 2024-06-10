-module(day1_part2).
-compile([no_auto_import, nowarn_unused_vars, nowarn_unused_function, nowarn_nomatch]).

-export([main/0]).

-spec get_list_of_lines(binary()) -> list(binary()).
get_list_of_lines(File_content) ->
    gleam@string:split(File_content, <<"\n"/utf8>>).

-spec compare_index({integer(), integer()}, {integer(), integer()}) -> gleam@order:order().
compare_index(Tuple1, Tuple2) ->
    {Index1, _} = Tuple1,
    {Index2, _} = Tuple2,
    case Index1 < Index2 of
        true ->
            lt;

        false ->
            case Index1 =:= Index2 of
                true ->
                    eq;

                false ->
                    gt
            end
    end.

-spec return_just_values(list({integer(), integer()}), list(integer())) -> list(integer()).
return_just_values(Inn_list, Out_list) ->
    case Inn_list of
        [Head | Tail] ->
            return_just_values(
                Tail,
                lists:append(Out_list, [erlang:element(2, Head)])
            );

        [] ->
            Out_list
    end.

-spec join_lists(list({integer(), integer()}), list({integer(), integer()})) -> list(integer()).
join_lists(List1, List2) ->
    List_comb = lists:append(List1, List2),
    return_just_values(gleam@list:sort(List_comb, fun compare_index/2), []).

-spec find_all_digits(list(binary()), integer(), list({integer(), integer()})) -> list({integer(),
    integer()}).
find_all_digits(Line, Index, Return_list) ->
    case Line of
        [_ | _] ->
            case gleam@int:parse(
                gleam@result:unwrap(gleam@list:first(Line), <<""/utf8>>)
            ) of
                {ok, Dig} ->
                    find_all_digits(
                        gleam@list:drop(Line, 1),
                        Index + 1,
                        lists:append(Return_list, [{Index, Dig}])
                    );

                {error, _} ->
                    find_all_digits(
                        gleam@list:drop(Line, 1),
                        Index + 1,
                        Return_list
                    )
            end;

        [] ->
            Return_list
    end.

-spec pars_dig_str_to_int(list(binary())) -> {ok, integer()} | {error, nil}.
pars_dig_str_to_int(Str) ->
    Possible_num = gleam@list:fold(
        Str,
        <<""/utf8>>,
        fun(A, B) -> <<A/binary, B/binary>> end
    ),
    case Possible_num of
        <<"one"/utf8>> ->
            {ok, 1};

        <<"two"/utf8>> ->
            {ok, 2};

        <<"three"/utf8>> ->
            {ok, 3};

        <<"four"/utf8>> ->
            {ok, 4};

        <<"five"/utf8>> ->
            {ok, 5};

        <<"six"/utf8>> ->
            {ok, 6};

        <<"seven"/utf8>> ->
            {ok, 7};

        <<"eight"/utf8>> ->
            {ok, 8};

        <<"nine"/utf8>> ->
            {ok, 9};

        <<"zero"/utf8>> ->
            {ok, 0};

        _ ->
            {error, nil}
    end.

-spec find_all_string_digits(
    list(binary()),
    integer(),
    list({integer(), integer()})
) -> list({integer(), integer()}).
find_all_string_digits(Line, Index, Return_list) ->
    case Line of
        [_, _, _ | _] ->
            case pars_dig_str_to_int(gleam@list:take(Line, 5)) of
                {ok, Dig} ->
                    find_all_string_digits(
                        gleam@list:drop(Line, 1),
                        Index + 1,
                        lists:append(Return_list, [{Index, Dig}])
                    );

                {error, nil} ->
                    case pars_dig_str_to_int(gleam@list:take(Line, 4)) of
                        {ok, Dig@1} ->
                            find_all_string_digits(
                                gleam@list:drop(Line, 1),
                                Index + 1,
                                lists:append(Return_list, [{Index, Dig@1}])
                            );

                        {error, nil} ->
                            case pars_dig_str_to_int(gleam@list:take(Line, 3)) of
                                {ok, Dig@2} ->
                                    find_all_string_digits(
                                        gleam@list:drop(Line, 1),
                                        Index + 1,
                                        lists:append(
                                            Return_list,
                                            [{Index, Dig@2}]
                                        )
                                    );

                                {error, nil} ->
                                    find_all_string_digits(
                                        gleam@list:drop(Line, 1),
                                        Index + 1,
                                        Return_list
                                    )
                            end
                    end
            end;

        _ ->
            Return_list
    end.

-spec string_to_list(binary()) -> list(binary()).
string_to_list(Line) ->
    gleam@string:to_graphemes(Line).

-spec number_in_line(binary()) -> integer().
number_in_line(Line) ->
    Line_as_list = string_to_list(Line),
    Digs = find_all_digits(Line_as_list, 0, []),
    Str_digs = find_all_string_digits(Line_as_list, 0, []),
    Com_list = join_lists(Digs, Str_digs),
    Num = gleam@int:undigits(
        [gleam@result:unwrap(gleam@list:first(Com_list), 0),
            gleam@result:unwrap(gleam@list:last(Com_list), 0)],
        10
    ),
    case Num of
        {ok, Num@1} ->
            Num@1;

        {error, _} ->
            0
    end.

-spec main() -> integer().
main() ->
    File_content = get_list_of_lines(
        gleam@result:unwrap(
            file:read_file(<<"./ts_t"/utf8>>),
            <<"No file here"/utf8>>
        )
    ),
    List_of_line_numbers = gleam@list:map(File_content, fun number_in_line/1),
    gleam@io:debug(
        gleam@list:fold(List_of_line_numbers, 0, fun(A, B) -> A + B end)
    ).
