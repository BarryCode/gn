{
  'variables': {
    'chromium_code': 1,
  },
  'targets': [
    {
      'target_name': 'gn_lib',
      'type': 'static_library',
      'dependencies': [
        '../../base/base.gyp:base',
      ],
      'sources': [
        'action_target_generator.cc',
        'action_target_generator.h',
        'action_values.cc',
        'action_values.h',
        'analyzer.cc',
        'analyzer.h',
        'args.cc',
        'args.h',
        'binary_target_generator.cc',
        'binary_target_generator.h',
        'build_settings.cc',
        'build_settings.h',
        'builder.cc',
        'builder.h',
        'builder_record.cc',
        'builder_record.h',
        'bundle_data.cc',
        'bundle_data.h',
        'bundle_data_target_generator.cc',
        'bundle_data_target_generator.h',
        'bundle_file_rule.cc',
        'bundle_file_rule.h',
        'c_include_iterator.cc',
        'c_include_iterator.h',
        'command_analyze.cc',
        'command_args.cc',
        'command_check.cc',
        'command_clean.cc',
        'command_desc.cc',
        'command_format.cc',
        'command_gen.cc',
        'command_help.cc',
        'command_ls.cc',
        'command_path.cc',
        'command_refs.cc',
        'commands.cc',
        'commands.h',
        'config.cc',
        'config.h',
        'config_values.cc',
        'config_values.h',
        'config_values_extractors.cc',
        'config_values_extractors.h',
        'config_values_generator.cc',
        'config_values_generator.h',
        'copy_target_generator.cc',
        'copy_target_generator.h',
        'create_bundle_target_generator.cc',
        'create_bundle_target_generator.h',
        'deps_iterator.cc',
        'deps_iterator.h',
        'desc_builder.cc',
        'desc_builder.h',
        'eclipse_writer.cc',
        'eclipse_writer.h',
        'err.cc',
        'err.h',
        'escape.cc',
        'escape.h',
        'exec_process.cc',
        'exec_process.h',
        'filesystem_utils.cc',
        'filesystem_utils.h',
        'function_exec_script.cc',
        'function_foreach.cc',
        'function_forward_variables_from.cc',
        'function_get_label_info.cc',
        'function_get_path_info.cc',
        'function_get_target_outputs.cc',
        'function_process_file_template.cc',
        'function_read_file.cc',
        'function_rebase_path.cc',
        'function_set_default_toolchain.cc',
        'function_set_defaults.cc',
        'function_template.cc',
        'function_toolchain.cc',
        'function_write_file.cc',
        'functions.cc',
        'functions.h',
        'functions_target.cc',
        'group_target_generator.cc',
        'group_target_generator.h',
        'header_checker.cc',
        'header_checker.h',
        'import_manager.cc',
        'import_manager.h',
        'inherited_libraries.cc',
        'inherited_libraries.h',
        'input_conversion.cc',
        'input_conversion.h',
        'input_file.cc',
        'input_file.h',
        'input_file_manager.cc',
        'input_file_manager.h',
        'item.cc',
        'item.h',
        'json_project_writer.cc',
        'json_project_writer.h',
        'label.cc',
        'label.h',
        'label_pattern.cc',
        'label_pattern.h',
        'label_ptr.h',
        'lib_file.cc',
        'lib_file.h',
        'loader.cc',
        'loader.h',
        'location.cc',
        'location.h',
        'ninja_action_target_writer.cc',
        'ninja_action_target_writer.h',
        'ninja_binary_target_writer.cc',
        'ninja_binary_target_writer.h',
        'ninja_build_writer.cc',
        'ninja_build_writer.h',
        'ninja_bundle_data_target_writer.cc',
        'ninja_bundle_data_target_writer.h',
        'ninja_copy_target_writer.cc',
        'ninja_copy_target_writer.h',
        'ninja_create_bundle_target_writer.cc',
        'ninja_create_bundle_target_writer.h',
        'ninja_group_target_writer.cc',
        'ninja_group_target_writer.h',
        'ninja_target_writer.cc',
        'ninja_target_writer.h',
        'ninja_toolchain_writer.cc',
        'ninja_toolchain_writer.h',
        'ninja_utils.cc',
        'ninja_utils.h',
        'ninja_writer.cc',
        'ninja_writer.h',
        'operators.cc',
        'operators.h',
        'output_file.cc',
        'output_file.h',
        'parse_node_value_adapter.cc',
        'parse_node_value_adapter.h',
        'parse_tree.cc',
        'parse_tree.h',
        'parser.cc',
        'parser.h',
        'path_output.cc',
        'path_output.h',
        'pattern.cc',
        'pattern.h',
        'pool.cc',
        'pool.h',
        'qt_creator_writer.cc',
        'qt_creator_writer.h',
        'runtime_deps.cc',
        'runtime_deps.h',
        'scheduler.cc',
        'scheduler.h',
        'scope.cc',
        'scope.h',
        'scope_per_file_provider.cc',
        'scope_per_file_provider.h',
        'settings.cc',
        'settings.h',
        'setup.cc',
        'setup.h',
        'source_dir.cc',
        'source_dir.h',
        'source_file.cc',
        'source_file.h',
        'source_file_type.cc',
        'source_file_type.h',
        'standard_out.cc',
        'standard_out.h',
        'string_utils.cc',
        'string_utils.h',
        'substitution_list.cc',
        'substitution_list.h',
        'substitution_pattern.cc',
        'substitution_pattern.h',
        'substitution_type.cc',
        'substitution_type.h',
        'substitution_writer.cc',
        'substitution_writer.h',
        'switches.cc',
        'switches.h',
        'target.cc',
        'target.h',
        'target_generator.cc',
        'target_generator.h',
        'template.cc',
        'template.h',
        'token.cc',
        'token.h',
        'tokenizer.cc',
        'tokenizer.h',
        'tool.cc',
        'tool.h',
        'toolchain.cc',
        'toolchain.h',
        'trace.cc',
        'trace.h',
        'unique_vector.h',
        'value.cc',
        'value.h',
        'value_extractors.cc',
        'value_extractors.h',
        'variables.cc',
        'variables.h',
        'visibility.cc',
        'visibility.h',
        'visual_studio_utils.cc',
        'visual_studio_utils.h',
        'visual_studio_writer.cc',
        'visual_studio_writer.h',
        'xcode_object.cc',
        'xcode_object.h',
        'xcode_writer.cc',
        'xcode_writer.h',
        'xml_element_writer.cc',
        'xml_element_writer.h',
      ],
    },
    {
      'target_name': 'gn',
      'type': 'executable',
      'sources': [
        'gn_main.cc',
      ],
      'dependencies': [
        'gn_lib',
        '../../base/base.gyp:base',
        '../../base/third_party/dynamic_annotations/dynamic_annotations.gyp:dynamic_annotations',
      ],
    },
    {
      'target_name': 'gn_unittests',
      'type': '<(gtest_target_type)',
      'sources': [
        'action_target_generator_unittest.cc',
        'analyzer_unittest.cc',
        'builder_unittest.cc',
        'c_include_iterator_unittest.cc',
        'command_format_unittest.cc',
        'config_unittest.cc',
        'config_values_extractors_unittest.cc',
        'escape_unittest.cc',
        'exec_process_unittest.cc',
        'filesystem_utils_unittest.cc',
        'function_foreach_unittest.cc',
        'function_forward_variables_from_unittest.cc',
        'function_get_label_info_unittest.cc',
        'function_get_path_info_unittest.cc',
        'function_get_target_outputs_unittest.cc',
        'function_process_file_template_unittest.cc',
        'function_rebase_path_unittest.cc',
        'function_toolchain_unittest.cc',
        'function_write_file_unittest.cc',
        'functions_target_unittest.cc',
        'functions_unittest.cc',
        'header_checker_unittest.cc',
        'inherited_libraries_unittest.cc',
        'input_conversion_unittest.cc',
        'label_pattern_unittest.cc',
        'label_unittest.cc',
        'loader_unittest.cc',
        'ninja_action_target_writer_unittest.cc',
        'ninja_binary_target_writer_unittest.cc',
        'ninja_bundle_data_target_writer_unittest.cc',
        'ninja_copy_target_writer_unittest.cc',
        'ninja_create_bundle_target_writer_unittest.cc',
        'ninja_group_target_writer_unittest.cc',
        'ninja_target_writer_unittest.cc',
        'ninja_toolchain_writer_unittest.cc',
        'operators_unittest.cc',
        'parse_tree_unittest.cc',
        'parser_unittest.cc',
        'path_output_unittest.cc',
        'pattern_unittest.cc',
        'runtime_deps_unittest.cc',
        'scope_per_file_provider_unittest.cc',
        'scope_unittest.cc',
        'source_dir_unittest.cc',
        'source_file_unittest.cc',
        'string_utils_unittest.cc',
        'substitution_pattern_unittest.cc',
        'substitution_writer_unittest.cc',
        'target_unittest.cc',
        'template_unittest.cc',
        'test_with_scope.cc',
        'test_with_scope.h',
        'tokenizer_unittest.cc',
        'unique_vector_unittest.cc',
        'value_unittest.cc',
        'visibility_unittest.cc',
        'visual_studio_utils_unittest.cc',
        'visual_studio_writer_unittest.cc',
        'xml_element_writer_unittest.cc',
      ],
      'dependencies': [
        'gn_lib',
        '../../base/base.gyp:run_all_unittests',
        '../../base/base.gyp:test_support_base',
        '../../testing/gtest.gyp:gtest',
      ],
    },
  ],
  'conditions': [
    ['test_isolation_mode != "noop"', {
      'targets': [
        {
          'target_name': 'gn_unittests_run',
          'type': 'none',
          'dependencies': [
            'gn_unittests',
          ],
          'includes': [ '../../build/isolate.gypi' ],
          'sources': [ 'gn_unittests.isolate' ],
        },
      ],
    }],
  ],
}
